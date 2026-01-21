# MCP Server 환율 에이전트 예제 (ADK)

이 디렉토리는 Streamable HTTP 전송을 사용하여 MCP(Model Context Protocol)를 통해 간단한 도구를 노출하는 방법을 보여주는 예제 ADK(Agent Development Kit) 설정을 포함하고 있습니다. 이 예제는 Frankfurter API를 호출하여 환율 정보를 반환하는 작은 MCP 서버를 제공합니다.

## .env 구성

예제는 환경 구성이 저장소 루트 또는 상위 `04-mcp` 디렉토리의 `.env` 파일에 있을 것으로 예상합니다. 권장 변수 및 인증 단계는 ADK 빠른 시작을 참조하세요:
https://google.github.io/adk-docs/get-started/quickstart/#set-up-the-model

ADK 예제에서 사용되는 일반적인 환경 변수:
```
GOOGLE_GENAI_USE_VERTEXAI=TRUE
GOOGLE_CLOUD_PROJECT=your-project-id
GOOGLE_CLOUD_LOCATION=global
GOOGLE_GENAI_MODEL=gemini-2.5-flash

# 또는 AI Studio 사용 시:
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=PASTE_YOUR_ACTUAL_API_KEY_HERE
```

## 로컬에서 MCP 서버 실행 방법

### Cloud Run 기반으로 Streamable MCP 서버 기동.

마찬가지로 셸에서 GCP 인증이 필요합니다:
```
gcloud auth application-default login
```

먼저 mcp_server 안에 있는 remote_server.py 파일을 GCP Cloud run 위에 기동을 해야 합니다.
실행 방법은 아래와 같습니다.

```
adk/04-mcp/streamable_http/mcp_server $ . ./deploy.sh
```

정상적으로 기동이 되었다면 GCP console 에서 확인이 가능합니다. 

### ADK agent 에서 Streamable MCP 서버 접속 및 실행.

마찬가지로 셸에서 GCP 인증이 필요합니다:
```
gcloud auth application-default login
```

다음 명령어로 ADK 에이전트 예제를 실행하세요:
```
adk/04-mcp $ adk web
```

"2025년 8월 14일의 원-달러 환율을 보여줘."라고 질문해 보세요.

## 라이선스

이 프로젝트는 Apache License 2.0을 따릅니다. 모든 코드와 콘텐츠의 저작권은 **ForusOne**(shins777@gmail.com)에 있습니다.
