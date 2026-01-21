# ADK 04-mcp 가이드

이 디렉토리는 다양한 전송 및 서버 스타일을 사용하여 모델 컨텍스트 프로토콜(MCP) 도구를 노출하고 사용하는 방법을 보여주는 예제와 유틸리티를 포함하고 있습니다. 예제에는 서버 구현(stdio 및 Streamable HTTP)과 해당 서버에 연결하는 클라이언트 측 예제가 모두 포함되어 있습니다.

## 개요
MCP를 사용하면 에이전트와 도구가 표준화된 프로토콜을 사용하여 통신할 수 있습니다. 이 폴더는 다음 작업을 수행할 때 유용한 참조 구현을 제공합니다:
- MCP를 통해 사용자 지정 도구(FunctionTool, 래퍼)를 원격 에이전트에 노출합니다.
- 로컬 테스트 또는 배포(예: Cloud Run)에 적합한 다양한 전송(stdio, Streamable HTTP)을 사용하여 MCP 서버를 실행합니다.
- 원격 도구를 사용하는 경량 MCP 클라이언트를 빌드하거나 테스트합니다.

## 폴더 및 예제 요약

### streamable_http
- 목적: Streamable HTTP MCP 서버 및 유틸리티 예제.
- 주요 파일: `mcp_server/remote_server.py`, `mcp_server/Dockerfile`
- 설명: Streamable HTTP MCP 엔드포인트(`/mcp`)를 마운트하는 Starlette + uvicorn ASGI 앱입니다. 이 예제는 `get_exchange_rate` 도구(Frankfurter API)를 광고하고 이벤트 루프 외부에서 차단 호출을 안전하게 실행하는 방법을 보여줍니다. Dockerfile은 Cloud Run에 적합한 컨테이너를 빌드하는 방법을 보여줍니다.

### stdio (stdio MCP 서버 예제)
- 목적: stdio를 통해 실행되는 MCP 서버 예제(로컬 프로세스 기반 설정 및 간단한 테스트에 유용).
- 주요 파일: FunctionTool 래퍼를 노출하고 `list_tools` 및 `call_tool` 핸들러를 시연하는 MCP stdio 서버를 구현하는 예제입니다.
- 설명: 하위 프로세스 기반 MCP 전송을 통해 에이전트에 도구를 노출하는 방법을 배우는 데 유용합니다.

### mcp_client
- 목적: MCP 서버에 연결하고 프로그래밍 방식으로 도구를 호출하는 MCP 클라이언트 예제.
- 주요 파일: MCP 기반 도구를 사용하는 클라이언트 구현 및 예제 에이전트.
- 설명: 파일 브라우저 스타일 에이전트 및 MCP 연결 매개변수를 사용하여 stdio 또는 Streamable HTTP 서버와 통신하는 방법을 보여주는 기타 작은 클라이언트를 포함합니다.

### mcp_client_server
- 목적: Python MCP 서버와 상호 작용하는 클라이언트 에이전트를 시연하는 종단 간 클라이언트+서버 예제.
- 주요 파일: 클라이언트 측 에이전트 예제 및 서버 구현(환율 도구 예제).

### mcp_google_map
- 목적: Google Maps 기능을 MCP 도구로 래핑하는 방법을 보여주는 예제.
- 주요 파일: 에이전트 래퍼 및 작은 서버/런처 예제.
- 참고: 환경에 유효한 `GOOGLE_MAPS_API_KEY`가 설정되어 있어야 합니다. 일부 구성에서는 `npx`를 사용하여 로컬 도우미를 실행할 수 있습니다. 자세한 내용 및 보안 고려 사항은 해당 하위 폴더의 README를 확인하세요.


## 예제 실행 방법

해당 예제 및 특정 에이전트 또는 서버를 실행하는 방법에 대한 자세한 내용은 각 하위 폴더 내의 README 및 소스 파일을 확인하세요.

## 라이선스
이 프로젝트는 Apache License 2.0 라이선스를 따릅니다. 모든 코드와 콘텐츠의 저작권은 **ForusOne**(shins777@gmail.com)에 있습니다.