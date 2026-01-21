import asyncio
import json
from dotenv import load_dotenv

from mcp import types as mcp_types 
from mcp.server.lowlevel import Server, NotificationOptions
from mcp.server.models import InitializationOptions
import mcp.server.stdio

from google.adk.tools.function_tool import FunctionTool
from google.adk.tools.mcp_tool.conversion_utils import adk_to_mcp_tool_type

load_dotenv()

mcp_svr_app = None
exchange_rate_tool = None 

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
    import requests
    response = requests.get(
        f"https://api.frankfurter.app/{currency_date}",
        params={"from": currency_from, "to": currency_to},
    )
    return response.json()

#-----------------------[mcp_server_init]-----------------------

def mcp_server_init():
    """
    MCP 서버 및 ADK 환율 도구를 초기화합니다.
    이 함수는 환율 쿼리를 위한 ADK FunctionTool을 생성하고 초기화 메시지를 출력합니다.
    그런 다음 MCP 서버 인스턴스를 생성하고 초기화된 도구와 함께 반환하여 MCP를 통해 노출합니다.

    Returns:
        tuple: MCP 서버 인스턴스와 초기화된 환율 도구를 포함하는 튜플.
    """

    exchange_rate_tool = FunctionTool(func=get_exchange_rate)

    print("ADK 환율 도구 초기화 중...")
    print(f"ADK 도구 '{exchange_rate_tool.name}' 초기화됨.")

    # --- MCP 서버 설정 ---
    print("MCP 서버 인스턴스 생성 중...")
    mcp_svr_app = Server("adk-exchange-rate-mcp-server") 
    print("MCP 서버 인스턴스 생성됨.")

    return mcp_svr_app, exchange_rate_tool

mcp_svr_app, exchange_rate_tool = mcp_server_init()

#-----------------------[list_tools]-----------------------
@mcp_svr_app.list_tools()
async def list_tools() -> list[mcp_types.Tool]:
    """
    사용 가능한 도구 목록을 반환하는 MCP 핸들러입니다.

    이 함수는 MCP 서버가 사용 가능한 도구 목록을 제공해야 할 때 호출됩니다.
    ADK 도구 정의를 MCP 도구 스키마 형식으로 변환하여 목록으로 반환합니다.
    이를 통해 클라이언트는 서버에서 노출하는 도구를 확인할 수 있습니다.

    Returns:
        list[mcp_types.Tool]: 사용 가능한 MCP 도구 스키마 목록입니다.
    """

    print("MCP 서버: list_tools 요청 수신됨.")
    # ADK 도구의 정의를 MCP 형식으로 변환
    mcp_tool_schema = adk_to_mcp_tool_type(exchange_rate_tool)
    print(f"MCP 서버: 도구 광고 중: {mcp_tool_schema.name}")
    return [mcp_tool_schema]

#-----------------------[call_tool]-----------------------
@mcp_svr_app.call_tool()
async def call_tool(
    name: str, arguments: dict
) -> list[mcp_types.TextContent | mcp_types.ImageContent | mcp_types.EmbeddedResource]:
    """
    도구 실행 요청을 처리하는 MCP 핸들러입니다.

    이 함수는 클라이언트가 도구 실행을 요청할 때 호출됩니다.
    요청된 도구 이름이 ADK 도구와 일치하면 비동기적으로 실행되고 결과는 MCP 콘텐츠 형식으로 반환됩니다.
    도구를 찾을 수 없거나 오류가 발생하면 MCP 형식의 오류 메시지가 반환됩니다.

    Args:
        name (str): 실행할 도구의 이름
        arguments (dict): 도구에 전달할 인수
    Returns:
        list[mcp_types.TextContent | mcp_types.ImageContent | mcp_types.EmbeddedResource]:
            MCP 콘텐츠로 포맷된 도구 응답 목록
    """

    print(f"MCP 서버: '{name}'에 대한 call_tool 요청 수신됨. 인수: {arguments}")

    # 요청된 도구 이름이 래핑된 ADK 도구와 일치하는지 확인
    if name == exchange_rate_tool.name:
        try:
            # ADK 도구의 run_async 메서드 실행
            # 참고: tool_context는 전체 ADK Runner 호출이 아니므로 None이 사용됩니다.
            adk_response = await exchange_rate_tool.run_async(
                args=arguments,
                tool_context=None, # 여기서는 ADK 컨텍스트 없음
            )
            print(f"MCP 서버: ADK 도구 '{name}' 성공적으로 실행됨.")
            # ADK 도구의 응답(일반적으로 딕셔너리)을 MCP 형식으로 변환
            # 여기서 응답 딕셔너리는 JSON 문자열로 직렬화되고 TextContent에 래핑됩니다.
            # 실제 도구 출력 및 클라이언트 요구 사항에 따라 포맷을 조정하세요.
            response_text = json.dumps(adk_response, indent=2)
            return [mcp_types.TextContent(type="text", text=response_text)]

        except Exception as e:
            print(f"MCP 서버: ADK 도구 '{name}' 실행 중 오류 발생: {e}")
            # MCP 형식으로 오류 메시지 반환
            # 더 강력한 MCP 오류 응답을 구현할 수 있습니다.
            error_text = json.dumps({"error": f"Failed to execute tool '{name}': {str(e)}"})
            return [mcp_types.TextContent(type="text", text=error_text)]
    else:
        # 알 수 없는 도구 호출 처리
        print(f"MCP 서버: 도구 '{name}'를 찾을 수 없습니다.")
        error_text = json.dumps({"error": f"Tool '{name}' not implemented."})
        # 단순히 오류를 TextContent로 반환
        return [mcp_types.TextContent(type="text", text=error_text)]

#-----------------------[run_server]-----------------------
async def run_server():
    """
    표준 입/출력을 사용하여 MCP 서버를 실행합니다.

    이 함수는 MCP 라이브러리의 stdio_server 컨텍스트 관리자를 사용하여 서버를 시작하고 핸드셰이크를 수행한 다음, 요청 및 도구 실행을 처리하기 위해 메인 이벤트 루프로 진입합니다.
    MCP 서버 프로세스의 메인 진입점으로 사용됩니다.

    Returns:
        None
    """
  
    # MCP 라이브러리의 stdio_server 컨텍스트 관리자 사용
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        print("MCP 서버 핸드셰이크 시작 중...")
        # MCP 서버 실행 루프 시작.
        # 이 호출은 제공된 읽기/쓰기 스트림을 사용하여 프로토콜 핸드셰이크를 수행하고,
        # 제공된 InitializationOptions(이름, 버전, 기능)를 통해 서버를 등록한 다음,
        # 메인 비동기 메시지 처리 루프로 진입합니다.
        # 실행되는 동안 MCP 서버는 수신되는 MCP 메시지(예: list_tools, call_tool)를 수신하고,
        # 위에 정의된 등록된 핸들러로 디스패치하고,
        # 쓰기 스트림을 통해 응답을 다시 씁니다. 호출은 클라이언트가 연결을 끊거나 스트림이 닫힐 때 완료됩니다.
        #
        # 참고: `read_stream` 및 `write_stream`은 하위 프로세스 stdio(`mcp.server.stdio.stdio_server()`에서)에 연결되므로
        # 하위 프로세스 기반 MCP 전송에 적합합니다.
        await mcp_svr_app.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name=mcp_svr_app.name, # 위에 정의된 서버 이름 사용
                server_version="0.1.0",
                capabilities=mcp_svr_app.get_capabilities(
                    # 서버 기능 정의 - MCP 문서 참조
                    notification_options=NotificationOptions(),
                    experimental_capabilities={},
                ),
            ),
        )
        print("MCP 서버 실행 루프 종료됨.")


if __name__ == "__main__":
    print("ADK 도구를 노출하는 MCP 서버 시작 중...")
    try:
        asyncio.run(run_server())
    except KeyboardInterrupt:
        print("\n사용자에 의해 MCP 서버 중지됨.")
    except Exception as e:
        print(f"MCP 서버에 오류 발생: {e}")
    finally:
        print("MCP 서버 프로세스 종료 중.")
