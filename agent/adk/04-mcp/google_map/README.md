# ADK MCP Google Maps 도구 예제 (04-mcp/google_map)

이 예제는 **Model Context Protocol (MCP)**을 통해 Google Maps의 강력한 기능을 에이전트에 통합하는 방법을 보여줍니다.

## 주요 개념

- **MCP Google Maps Server**: `@modelcontextprotocol/server-google-maps` 패키지를 사용하여 장소 검색, 길찾기 등 지형 정보 서비스를 활용합니다.
- **API 통합**: 환경 변수로 설정된 Google Maps API 키를 MCP 서버에 안전하게 전달합니다.

## 주요 구성 요소

### 1. 에이전트 정의 (`agent.py`)
- **`mcp_google_map` 함수**: 
    - `GOOGLE_MAPS_API_KEY` 환경 변수를 확인하고 로드합니다.
    - `npx`를 통해 Google Maps MCP 서버를 실행하며, API 키를 서버의 환경 변수로 전달하여 `MCPToolset`을 구성합니다.
- **`mcp_google_map_tool`**: 지점 찾기, 길찾기, 장소 세부 정보 조회 등 Google Maps에서 제공하는 도구들을 포함합니다.
- **`root_agent`**: 지도 및 장소 관련 사용자 질문에 답변하기 위해 이 도구 세트를 사용합니다.

## 사전 준비 사항

- **Google Cloud API Key**: [Google Cloud Console](https://console.cloud.google.com/)에서 Google Maps Platform API 키를 발급받아야 합니다.
- **환경 변수 설정**: 프로젝트 루트 또는 본 폴더의 `.env` 파일에 `GOOGLE_MAPS_API_KEY`를 설정하세요.
- **Node.js**: `npx` 실행 환경이 필요합니다.

## 실행 방법

1. `.env` 파일에 유효한 API 키가 설정되어 있는지 확인합니다.
2. `04-mcp` 폴더에서 `adk web`을 실행합니다.
3. 에이전트 목록에서 `google_map`을 선택하여 다음과 같은 질문을 테스트합니다:
   - "서울역에서 강남역까지 가는 길을 알려줘."
   - "뉴욕 타임스퀘어 근처의 맛집을 찾아줘."

## 주의 사항
- **실험적 기능**: Google Maps MCP 서버는 현재 실험적 단계일 수 있으므로 사용 전 문서와 할당량을 확인하세요.
- **보안**: API 키가 코드나 버전 관리 시스템에 직접 노출되지 않도록 주의하세요.

## 라이선스
이 프로젝트는 Apache License 2.0을 따릅니다.