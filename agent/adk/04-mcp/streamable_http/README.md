# ADK MCP Streamable HTTP 원격 서버 예제 (04-mcp/streamable_http)

이 예제는 MCP 서버를 로컬 프로세스가 아닌 **원격 HTTP 서비스(Cloud Run 등)**로 배포하고, 에이전트가 이를 호출하는 현대적인 분산 에이전트 아키텍처를 보여줍니다.

## 주요 개념

- **Streamable HTTP**: 표준 HTTP 프로토콜 위에 스트리밍 데이터 전송 기능을 더해, 지연 시간이 긴 원격 작업에서도 실시간 상호작용이 가능하게 하는 MCP 전송 방식입니다.
- **Remote Host**: MCP 서버를 Cloud Run과 같은 서버리스 환경에 배포하여 언제 어디서나 호출 가능하게 합니다.

## 주요 구성 요소

### 1. 에이전트(클라이언트) 정의 (`agent.py`)
- **`mcp_streamable_http_tool` 함수**: 원격지 URL을 가리키는 `StreamableHTTPConnectionParams`를 사용하여 `MCPToolset`을 생성합니다.
- **`root_agent`**: 웹상에 떠 있는 원격 MCP 도구들을 마치 로컬 도구처럼 활용합니다.

### 2. 원격 MCP 서버 실체 (`mcp_server/remote_server.py`)
- **Starlette & Uvicorn**: 비동기 웹 프레임워크를 사용하여 HTTP 인터페이스를 제공합니다.
- **`StreamableHTTPSessionManager`**: MCP 프로토콜을 HTTP 스트림으로 변환하여 실시간 통신 세션을 관리합니다.
- **`stateless=True`**: 서버리스(Cloud Run)의 수평 확장에 유리하도록 상태 비저장 방식으로 구동됩니다.

## 워크플로우 동작 방식
1. 클라이언트 에이전트가 질문을 받습니다.
2. 도구 호출이 필요하면 설정된 URL로 HTTP POST 요청을 보냅니다.
3. 원격 서버가 요청을 받아 비동기로 로직(예: 환율 조회)을 수행합니다.
4. 결과가 스트림을 통해 클라이언트에 전달되고, 에이전트가 최종 응답을 생성합니다.

## 배포 및 테스트
이 예제에는 Cloud Run에 배포할 수 있는 설정 파일들이 포함되어 있습니다.
- **`Dockerfile`**: 서버 환경 구성.
- **`deploy.sh`**: Cloud Run 배포 스크립트.

## 실행 방법

1. 이미 배포된 서버가 있다면 `agent.py`의 `url` 주소를 해당 주소로 수정합니다.
2. `04-mcp` 폴더에서 `adk web`을 실행합니다.
3. 에이전트 목록에서 `streamable_http`를 선택하여 원격 도구 호출을 확인합니다.

## 기술적 참고 사항
- **서버리스 최적화**: `stateless` 설정과 `lifespan` 관리를 통해 Cloud Run과 같은 환경에서 효율적으로 동작하도록 설계되었습니다.
- **보안**: 프로덕션 환경에서는 HTTP 헤더를 통한 인증 과정이 추가되어야 합니다.

## 라이선스
이 프로젝트는 Apache License 2.0을 따릅니다.
