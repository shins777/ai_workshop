# Copyright 2025 Forusone(shins777@gmail.com)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import contextlib
import logging
import asyncio
from collections.abc import AsyncIterator
from typing import Any

import requests
import mcp.types as types
from mcp.server.lowlevel import Server
from mcp.server.streamable_http_manager import StreamableHTTPSessionManager
from starlette.applications import Starlette
from starlette.routing import Mount
from starlette.types import Receive, Scope, Send

logger = logging.getLogger(__name__)

#-----------------------[get_exchange_rate]-----------------------
def get_exchange_rate(
    currency_from: str = "USD",
    currency_to: str = "KRW",
    currency_date: str = "latest", )->dict:
    """
    지정된 날짜에 대한 두 통화 간의 환율을 검색합니다.

    Frankfurter API(https://api.frankfurter.app/)를 사용하여 환율 데이터를 가져옵니다.

    Args:
        currency_from: 기준 통화 (3자리 통화 코드). 기본값은 "USD"(미국 달러)입니다.
        currency_to: 대상 통화 (3자리 통화 코드). 기본값은 "KRW"(대한민국 원)입니다.
        currency_date: 환율을 조회할 날짜입니다. 기본값은 "latest"로 가장 최근 환율을 조회합니다.
            과거 환율의 경우 YYYY-MM-DD 형식으로 지정하세요.

    Returns:
        dict: 환율 정보를 포함하는 사전입니다.
            예: {"amount": 1.0, "base": "USD", "date": "2023-11-24", "rates": {"EUR": 0.95534}}
    """
    response = requests.get(
        f"https://api.frankfurter.app/{currency_date}",
        params={"from": currency_from, "to": currency_to},
    )
    return response.json()

#-----------------------[create_mcp_server]-----------------------
def create_mcp_server():
    """
    Model Context Protocol(MCP)을 통해 도구를 노출하는 MCP 서버 인스턴스를 생성하고 구성합니다.

    이 함수는 "adk-mcp-streamable-server"라는 이름의 `Server`를 빌드하고 반환하며 다음 핸들러를 등록합니다.

    - call_tool: 클라이언트가 도구 실행을 요청할 때 호출되는 비동기 핸들러입니다. 예제 구현은
      `asyncio.to_thread()`를 사용하여 이벤트 루프를 차단하지 않고 외부 API에 대한 차단 HTTP 요청을 수행하고 결과를 MCP TextContent로 래핑하여 반환하는 `get_exchange_rate` 도구를 지원합니다.
    - list_tools: 사용 가능한 도구 목록과 입력 스키마를 반환합니다(예제는 `get_exchange_rate`를 광고함).

    반환된 `Server`는 StreamableHTTPSessionManager(또는 다른 MCP 전송)와 함께 사용되어
    Streamable HTTP를 통해 클라이언트 연결을 수락하도록 의도되었습니다.

    Returns:
        Server: 구성된 MCP 서버 인스턴스.
    """

    app = Server("adk-mcp-streamable-server")


    @app.call_tool()
    async def call_tool(name: str, arguments: dict[str, Any]) -> list[types.ContentBlock]:
        """
        MCP 클라이언트의 도구 실행 요청을 처리합니다.

        이 비동기 핸들러는 MCP 클라이언트가 명명된 도구의 실행을 요청할 때 호출됩니다.
        함수는 `name` 매개변수를 검사하고 해당 도구 로직을 실행한 다음
        MCP ContentBlock 객체(예: TextContent, ImageContent) 목록을 반환해야 합니다.

        이 예제에서 지원되는 도구:
        - "get_exchange_rate": `currency_from`, `currency_to`, 및 `currency_date` 인수를 예상합니다.
          핸들러는 환율을 검색하기 위해 Frankfurter API에 대한 차단 HTTP 요청을 수행하고
          `asyncio.to_thread()`를 사용하여 차단 호출을 이벤트 루프 외부에서 실행합니다.

        Parameters:
            name (str): 클라이언트가 요청한 도구 식별자.
            arguments (dict[str, Any]): 도구 실행을 위해 클라이언트가 제공한 인수.

        Returns:
            list[types.ContentBlock]: MCP 콘텐츠 블록으로 포맷된 도구 출력이 포함된 목록.

        오류가 발생하면 핸들러는 예외를 발생시키는 대신 실패를 설명하는 TextContent 블록을 반환하여
        MCP 클라이언트가 기계 판독 가능한 오류 메시지를 수신하도록 합니다.
        """

        print(f"### 도구 호출됨: {name}, 인수: {arguments}")

        if name == "get_exchange_rate":
            
            print(f"### 인수와 함께 도구 {name} 선택됨: {arguments}")

            currency_from = arguments.get("currency_from", "USD")
            currency_to = arguments.get("currency_to", "KRW")
            currency_date = arguments.get("currency_date", "latest")

            # 비동기 이벤트 루프 차단을 방지하기 위해 스레드에서 차단 HTTP 호출 실행
            try:
                result = await asyncio.to_thread(get_exchange_rate, currency_from, currency_to, currency_date)
                print("### 도구 %s 실행 결과: %s", name, result)
                return [
                    types.TextContent(
                        type="text",
                        text=f"The exchange rate is : {result}"
                    )
                ]
            except Exception as e:
                print("### 도구 %s 실행 중 오류 발생: %s", name, e)
                # MCP TextContent 형식으로 클라이언트에 오류 메시지 반환
                return [
                    types.TextContent(
                        type="text",
                        text=f"도구 '{name}' 실행 오류: {str(e)}"
                    )
                ]
        else:
            raise ValueError(f"알 수 없는 도구: {name}")

    @app.list_tools()
    async def list_tools() -> list[types.Tool]:
        """
        이 MCP 서버에 의해 노출된 도구 목록을 반환합니다.

        MCP 클라이언트는 이 핸들러를 호출하여 서버에서 사용할 수 있는 도구를 검색하고
        각 도구의 설명 및 입력 스키마를 얻습니다. 반환된 목록은
        도구 이름, 설명 및 입력 JSON 스키마를 설명하는 `mcp.types.Tool` 객체를 포함해야 합니다.

        이 예제에서 서버는 단일 도구를 광고합니다:
        - "get_exchange_rate": `currency_from`, `currency_to`, 및 `currency_date` 입력 필드가 필요합니다.

        Returns:
            list[types.Tool]: MCP 클라이언트가 검색 및 유효성 검사에 사용할 수 있는 도구 설명자 목록입니다.
        """

        return [
            types.Tool(
                name="get_exchange_rate",
                description="지정된 날짜에 대한 두 통화 간의 환율을 검색합니다.",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "currency_from": {
                            "type": "string",
                            "description": "기준 통화 (3자리 통화 코드). 기본값은 'USD' (미국 달러)"
                        },
                        "currency_to": {
                            "type": "string",
                            "description": "대상 통화 (3자리 통화 코드). 기본값은 'KRW' (대한민국 원)"
                        },                        
                        "currency_date": {
                            "type": "string",
                            "description": "환율을 조회할 날짜입니다. 기본값은 'latest'로 가장 최근 환율을 조회합니다. 과거 환율의 경우 YYYY-MM-DD 형식으로 지정하세요."
                        },                        
                    },
                    "required": ["currency_from", "currency_to", "currency_date"],
                }
            )
        ]

    return app

#-----------------------[main]-----------------------

def main(json_response: bool = False):
    """
    MCP Streamable HTTP 서버를 실행합니다.

    이 함수는 로깅을 구성하고, MCP `Server`를 생성(`create_mcp_server()`를 통해)하고,
    `StreamableHTTPSessionManager`로 래핑합니다.
    Streamable HTTP 요청에 대한 ASGI 핸들러, 세션 관리자 수명 주기를 관리하기 위한
    수명 주기 컨텍스트 관리자를 정의하고, Starlette 애플리케이션의 `/mcp` 경로에 핸들러를 마운트하고,
    `uvicorn`을 사용하여 `0.0.0.0:8080`에서 애플리케이션을 시작합니다.

    Parameters:
        json_response (bool): True인 경우 StreamableHTTPSessionManager는 응답을 JSON 형식으로 반환합니다.
            이는 테스트나 디버깅에 유용할 수 있습니다. 기본값은 False입니다.

    Notes:
        - 서버는 서버리스 플랫폼(예: Cloud Run)에서의 더 나은 확장성을 위해 상태 비저장 모드로 구성됩니다.
        - 필요한 종속성에는 `mcp`, `starlette`, `uvicorn`, `requests`(예제 도구 구현용)가 포함됩니다.
        - 모듈 진입점으로 사용되도록 의도되었습니다 (`if __name__ == "__main__"`).

    Returns:
        None
    """

    logging.basicConfig(level=logging.INFO)

    app = create_mcp_server()

    # 확장성을 위해 상태 비저장 모드로 세션 관리자 생성
    session_manager = StreamableHTTPSessionManager(
        app=app,
        event_store=None,
        json_response=json_response,
        stateless=True,  # Cloud Run 확장성을 위해 중요
    )

    async def handle_streamable_http(scope: Scope, receive: Receive, send: Send) -> None:
        await session_manager.handle_request(scope, receive, send)

    @contextlib.asynccontextmanager
    async def lifespan(app: Starlette) -> AsyncIterator[None]:
        """세션 관리자 수명 주기 관리."""
        async with session_manager.run():
            logger.info("MCP Streamable HTTP 서버 시작됨!")
            try:
                yield
            finally:
                logger.info("MCP 서버 종료 중...")

    # ASGI 애플리케이션 생성
    starlette_app = Starlette(
        debug=False,  # 프로덕션의 경우 False로 설정
        routes=[
            Mount("/mcp", app=handle_streamable_http),
        ],
        lifespan=lifespan,
    )

    import uvicorn
    uvicorn.run(starlette_app, host="0.0.0.0", port=8080)

if __name__ == "__main__":
    main()