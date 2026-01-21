# Tavily 검색 도구 예제 (ADK)

이 폴더는 ADK(에이전트 개발 키트)에서 LangChain 기반 Tavily 검색 도구와 환율 조회 기능을 통합하여 에이전트가 웹 검색 및 환율 정보를 모두 조회할 수 있도록 하는 예제를 제공합니다. 또한 필요에 따라 다른 함수를 호출하는 방법을 보여줍니다.

## .env 설정

`.env` 파일은 상위 폴더(`03-tools`)에 위치해야 합니다. 환경 파일에 포함할 내용에 대한 자세한 내용은 다음 URL을 참조하세요:
https://google.github.io/adk-docs/get-started/quickstart/#set-up-the-model

다음은 엔터프라이즈 환경에서 Vertex AI와 함께 ADK를 사용하기 위한 예제 구성입니다:

```
GOOGLE_GENAI_USE_VERTEXAI=TRUE                  # 엔터프라이즈용 Vertex AI 사용.
GOOGLE_CLOUD_PROJECT="ai-hangsik"               # 자신의 Project ID로 변경하세요.
GOOGLE_CLOUD_LOCATION="global"                  # Global Endpoint 사용.
GOOGLE_GENAI_MODEL = "gemini-2.5-flash"         # 최신 Gemini 버전.

# Tavily API 키
TAVILY_API_KEY = "TAVILY_API_KEY"

```

AI Studio를 사용하는 일반 사용자의 경우 다음과 같이 GOOGLE_API_KEY를 설정하세요:

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
adk_workshop/adk/03-tools$ adk web
```

UI에서 langchain_tavily를 선택하고 다음 명령을 실행하세요:
```
이번주 대한민국 사회적 이슈에 대해서 설명해주고, 가장 최신 원달러 환율도 체크해줘.
```
## 라이선스

이 프로젝트는 Apache License 2.0을 따릅니다. 모든 코드와 콘텐츠의 저작권은 **ForusOne**(shins777@gmail.com)에 있습니다.
