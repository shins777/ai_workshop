# ADK MCP (Model Context Protocol) 통합 예제 (04-mcp)

이 디렉토리는 ADK(Agent Development Kit)가 **Model Context Protocol (MCP)**을 통해 다양한 외부 도구, 데이터 소스, 그리고 원격 서비스와 어떻게 상호작용하는지에 대한 종합적인 예제를 제공합니다.

MCP는 LLM 어플리케이션과 외부 데이터/도구 간의 인터페이스를 표준화한 프로토콜로, ADK는 이를 활용해 에이전트의 기능을 무궁무진하게 확장할 수 있습니다.

## 포함된 예제 및 학습 포인트

### 1. [FILESYSTEM (로컬 파일 시스템 관리)](./filesystem/README.md)
- **핵심**: 표준 Stdio MCP 서버 연동.
- **내용**: 에이전트가 지정된 로컬 폴더 내에서 파일을 읽고, 쓰고, 목록을 조회하는 파일 매니저 기능을 구현합니다.

### 2. [GOOGLE_MAP (구글 지도 인텔리전스)](./google_map/README.md)
- **핵심**: 외부 API 기반의 표준 MCP 서버 활용.
- **내용**: Google Maps Platform의 기능을 에이전트에 통합하여 장소 검색 및 길찾기 서비스를 제공합니다.

### 3. [LOCAL_SERVER (커스텀 MCP 서버 구축)](./local_server/README.md)
- **핵심**: ADK 도구를 MCP 환경으로 노출.
- **내용**: 기존의 ADK Python 도구를 MCP 서버로 래핑하여, 다른 ADK 클라이언트나 MCP 호환 앱에서 사용할 수 있게 하는 '서버-클라이언트' 구조를 실습합니다.

### 4. [MCP_TOOLBOX (중앙 집중식 도구 관리)](./mcp_toolbox/README.md)
- **핵심**: Toolbox 프레임워크와의 통합.
- **내용**: 수많은 도구를 YAML로 관리하고 동적으로 로드하여 BigQuery와 같은 엔터프라이즈 데이터 소스에 질의하는 고급 시나리오를 보여줍니다.

### 5. [STREAMABLE_HTTP (원격 및 클라우드 MCP)](./streamable_http/README.md)
- **핵심**: 분산 시스템 및 서버리스(Cloud Run) 배포.
- **내용**: MCP 서버를 HTTP 상에서 스트리밍 방식으로 제공하여, 물리적으로 떨어진 원격 에이전트가 도구를 호출하는 최신 아키텍처를 다룹니다.

---

## 공통 실행 및 테스트 방법

ADK는 모든 MCP 예제를 하나의 웹 인터페이스에서 통합 테스트할 수 있는 기능을 제공합니다.

1. `04-mcp` 폴더에서 명령어를 실행합니다:
   ```bash
   adk web
   ```
2. 웹 UI가 열리면, 왼쪽 에이전트 목록에서 테스트하고 싶은 예제(예: `google_map`, `local_server` 등)를 선택합니다.
3. 질문을 던지고, 에이전트가 MCP 서버와 통신하며 도구를 호출하는 과정을 실시간 로고와 추적 기능을 통해 확인하세요.

## 학습 순서 권장
1. **filesystem** 또는 **google_map**을 통해 표준 MCP 서버 사용법을 먼저 익히세요.
2. **local_server**를 통해 직접 MCP 서버를 만들어보는 과정을 학습하세요.
3. **streamable_http**를 통해 실제 서비스로 배포하는 아키텍처를 이해하세요.

## 라이선스
이 프로젝트는 Apache License 2.0을 따릅니다.