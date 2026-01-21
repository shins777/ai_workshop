# ADK 로컬 MCP 서버 예제 (04-mcp/local_server)

이 예제는 ADK의 기능을 MCP(Model Context Protocol) 서버로 노출하고, 이를 다른 ADK 에이전트에서 활용하는 **Custom MCP Server-Client** 아키텍처를 보여줍니다.

## 주요 개념

- **MCP Server Wrapper**: ADK의 `FunctionTool`을 MCP 표준 규격으로 감싸서 외부(stdio)에서 호출 가능하게 만듭니다.
- **Local Stdio Connection**: `python3 -m local_server.exchange_rate` 명령을 통해 로컬 프로세스를 MCP 서버로 구동하고 클라이언트와 통신합니다.

## 주요 구성 요소

### 1. MCP 서버 구현 (`exchange_rate.py`)
- **`get_exchange_rate`**: Frankfurter API를 연동하여 실시간 환율을 가져오는 내부 함수입니다.
- **`mcp_svr_app`**: Python `mcp` 라이브러리를 사용하여 서버 인스턴스를 생성하고, `list_tools` 및 `call_tool` 핸들러를 통해 ADK 도구를 MCP 프로토콜에 등록합니다.
- **Stdio 실행**: `asyncio.run(run_server())`를 통해 표준 입출력 기반의 서버를 구동합니다.

### 2. 에이전트(클라이언트) 정의 (`agent.py`)
- **`mcp_toolset` 함수**: `python3`를 통해 로컬의 `exchange_rate` 모듈을 실행하는 `MCPToolset`을 생성합니다.
- **`root_agent`**: 로컬 서버가 노출한 환율 도구를 사용하여 사용자의 환율 질문에 답변합니다.

## 워크플로우 동작 방식
1. 클라이언트(`agent.py`)가 구동될 때 `exchange_rate.py`를 하위 프로세스로 실행합니다.
2. 클라이언트 에이전트가 환율 도구가 필요하다고 판단하면 MCP를 통해 정보를 요청합니다.
3. 로컬 서버(`exchange_rate.py`)가 API를 호출하여 결과를 반환하고, 에이전트가 이를 취합하여 응답합니다.

## 실행 방법

1. `04-mcp` 폴더에서 `adk web`을 실행합니다.
2. 에이전트 목록에서 `local_server`를 선택합니다.
3. 다음과 같이 질문을 테스트합니다:
   - "현재 USD 대비 KRW 환율은 얼마인가요?"

## 기술적 참고 사항
- **`adk_to_mcp_tool_type`**: ADK의 전용 도구 유틸리티를 사용하여 ADK 도구 정의를 MCP JSON Schema로 자동 변환합니다.
- 이 패턴을 확장하면 기존에 Python으로 작성된 다양한 ADK 도구들을 표준 MCP 도구로 전환하여 다른 MCP 호환 플랫폼에서도 사용할 수 있게 됩니다.

## 라이선스
이 프로젝트는 Apache License 2.0을 따릅니다.