# MCP 서버 환율 에이전트 예제 (ADK)

이 폴더는 MCP(Model Context Protocol)를 사용하여 사용자 지정 Python MCP 서버에 연결하고 실시간 환율 정보를 검색하는 ADK(Agent Development Kit)의 에이전트 예제를 제공합니다.

## .env 구성

`.env` 파일을 상위 폴더(`04-mcp `)에 배치해야 합니다. 환경 파일에 포함할 내용에 대한 자세한 내용은 다음 URL을 참조하세요:
https://google.github.io/adk-docs/get-started/quickstart/#set-up-the-model

다음 환경 설정은 엔터프라이즈 환경에서 Vertex AI와 함께 ADK를 사용하기 위한 예제입니다:
```
GOOGLE_GENAI_USE_VERTEXAI=TRUE                  # 엔터프라이즈용 Vertex AI 사용.
GOOGLE_CLOUD_PROJECT="ai-hangsik"               # 자신의 Project ID로 변경하세요.
GOOGLE_CLOUD_LOCATION="global"                  # 글로벌 엔드포인트 사용.
GOOGLE_GENAI_MODEL = "gemini-2.5-flash"         # 최신 Gemini 모델.
```

`AI Studio`를 사용하는 일반 사용자의 경우 다음과 같이 GOOGLE_API_KEY를 설정하세요:
```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=PASTE_YOUR_ACTUAL_API_KEY_HERE
```
## 소스 코드 실행 방법
다음 gcloud 명령어를 사용하여 Google Cloud 인증을 설정하세요:
```
gcloud auth application-default login
```

다음 명령어로 하위 에이전트 도구 예제를 실행하세요:
```
adk_workshop/adk/04-mcp $ adk web
```

테스트를 위해 다음과 같은 질문을 사용하세요:
```
USD-KRW 환율을 알려줘.
```

## 예제 기능
- 사용자 쿼리에 응답하여 MCP 서버에 연결하여 실시간 환율 정보를 제공합니다.
- 다양한 통화 간의 환율을 검색하기 위해 Frankfurter API를 사용합니다.

## 라이선스

이 프로젝트는 Apache License 2.0을 따릅니다. 모든 코드와 콘텐츠의 저작권은 **ForusOne**(shins777@gmail.com)에 있습니다.