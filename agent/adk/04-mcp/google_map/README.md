# MCP Google Maps 도구 예제 (ADK)

이 폴더는 모델 컨텍스트 프로토콜(MCP)을 사용하여 Google Maps MCP 서버 도구를 ADK 에이전트와 통합하는 방법을 보여줍니다. 제공된 `agent.py`는 `npx`를 통해 `@modelcontextprotocol/server-google-maps` 서버를 시작하는 MCPToolset을 초기화하고 Google Maps 기능을 LLM 기반 에이전트에게 노출하는 방법을 보여줍니다.

> 참고: 이 예제는 실험적입니다. MCP 서버 구현 및 도구 동작은 시간이 지남에 따라 변경될 수 있습니다.

## .env 구성

`.env` 파일을 상위 폴더(`04-mcp `)에 배치하세요. 에이전트는 `GOOGLE_MAPS_API_KEY` 환경 변수를 통해 Google Maps API 키를 사용할 수 있을 것으로 예상합니다.

`.env` 항목 예시 (상위 `04-mcp ` 폴더):

```
# 환경에 따라 Vertex AI 또는 AI Studio 사용
GOOGLE_GENAI_USE_VERTEXAI=TRUE
GOOGLE_CLOUD_PROJECT="your-project-id"
GOOGLE_CLOUD_LOCATION="global"
GOOGLE_GENAI_MODEL="gemini-2.5-flash"

# MCP Google Maps 서버에서 사용하는 Google Maps API 키 제공
GOOGLE_MAPS_API_KEY=PASTE_YOUR_GOOGLE_MAPS_API_KEY_HERE
```

`GOOGLE_MAPS_API_KEY`가 설정되지 않은 경우, 에이전트는 자격 증명 없이 도구를 실행하는 것을 방지하기 위해 오류를 발생시킵니다.

## 요구 사항

- Node.js / npx 설치 됨 (MCP Google Maps 서버는 `npx`로 시작됨).
- 필수 Maps API가 활성화된 유효한 Google Maps API 키.
- 메인 프로젝트 README에 따라 설치된 ADK 환경 및 종속성.

## 실행 방법

1. Vertex AI 또는 기타 GCP 리소스를 사용하는 경우 Google Cloud 인증:

```
gcloud auth application-default login
```

2. `04-mcp `의 `.env` 파일에 유효한 `GOOGLE_MAPS_API_KEY` 및 기타 필수 항목이 포함되어 있는지 확인하세요.

3. ADK 웹 서버를 실행하여 도구 및 에이전트 로드:

```
adk_workshop/adk/04-mcp $ adk web
```

에이전트가 초기화되면 `npx @modelcontextprotocol/server-google-maps`를 통해 Google Maps MCP 서버를 시작하는 MCPToolset을 생성하고 `GOOGLE_MAPS_API_KEY`를 서버 프로세스 환경에 주입합니다.

## 사용법

- ADK 웹 UI를 시작한 후 Google Maps / MCP 에이전트(`agent.py`의 에이전트 이름은 `Assistant_agent_Google_Map`)를 선택하세요.
- 다음과 같은 지도 관련 질문을 하세요:

```
내 현재 위치에서 가장 가까운 커피숍을 찾아줘.
```

또는

```
뉴욕 센트럴 파크에서 뉴욕 타임스 스퀘어까지 가는 길을 알려줘.
```

에이전트는 적절한 요청을 MCP Google Maps 서버로 전달하고 결과를 반환합니다.

## 보안 고려 사항

- 소스 제어에 API 키를 커밋하지 마세요. 항상 환경 변수 또는 보안 비밀 저장소를 사용하세요.
- 프로덕션의 경우 API 키를 승인된 HTTP 리퍼러 또는 IP 주소로 제한하고 필요한 Maps API만 활성화하세요.

## 문제 해결

- 에이전트가 `RuntimeError: GOOGLE_MAPS_API_KEY is not set.`를 발생시키면 `.env` 파일이 상위 `04-mcp ` 폴더에 있고 유효한 `GOOGLE_MAPS_API_KEY` 항목이 포함되어 있는지 확인하세요.
- `npx`가 시스템 PATH에서 사용 가능한지, 그리고 `@modelcontextprotocol/server-google-maps`가 컴퓨터에서 실행될 수 있는지 확인하세요.
- 서버 시작 로그 및 오류 메시지는 브라우저 콘솔 및 `adk web`을 실행하는 터미널을 확인하세요.

## 라이선스

이 프로젝트는 Apache License 2.0을 따릅니다. 모든 코드와 콘텐츠의 저작권은 **ForusOne**(shins777@gmail.com)에 있습니다.