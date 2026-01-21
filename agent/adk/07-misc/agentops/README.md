# ADK Observability 예제 - AgentOps 설정

이 폴더는 ADK(에이전트 개발 키트) 프레임워크로 구축된 AI 에이전트에서 관측성(observability)을 위해 AgentOps를 사용하는 방법에 대한 예제를 제공합니다.
이 코드를 실행하려면 AgentOps 사이트에 가입하고 토큰을 발급받아야 합니다:
* https://app.agentops.ai/

API_KEY를 받으면 아래와 같이 .env 파일에 설정하세요.

## .env 설정

`.env` 파일은 상위 폴더(`10-observability`)에 위치해야 합니다. 환경 파일에 포함할 내용에 대한 자세한 내용은 다음 URL을 참조하세요:
https://google.github.io/adk-docs/get-started/quickstart/#set-up-the-model

다음은 엔터프라이즈 환경에서 Vertex AI와 함께 ADK를 사용하기 위한 예제 구성입니다:

```
GOOGLE_GENAI_USE_VERTEXAI = TRUE
GOOGLE_CLOUD_PROJECT = "YOUR_PROJECT_ID"
GOOGLE_CLOUD_LOCATION = "YOUR_PROJECT_LOCATION"
GOOGLE_GENAI_MODEL = "gemini-2.5-flash"

AGENTOPS_API_KEY="0000000-0000-0000-0000-000000" # AgentOps 키
```

AI Studio를 사용하는 일반 사용자의 경우 다음과 같이 GOOGLE_API_KEY를 설정하세요:

```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=PASTE_YOUR_ACTUAL_API_KEY_HERE
```

## 에이전트 파일 구조
```
adk/10-observability/agentops/
├── __init__.py
├── agent.py
└── README.md
```

- `agent.py`: AgentOps가 설정된 에이전트의 빌드 코드를 포함합니다.
- `__init__.py`: 폴더를 Python 패키지로 표시합니다.

## 예제 실행

다음 gcloud 명령어를 사용하여 Google Cloud 인증을 설정하세요:

```
gcloud auth application-default login
```

`10-observability` 폴더에서 아래 명령어를 실행하고 adk 웹 인터페이스에서 테스트하세요:

```
adk_workshop/adk/10-observability$ adk web
```

## 라이선스
이 프로젝트는 Apache License 2.0을 따릅니다. 모든 코드와 콘텐츠의 저작권은 **ForusOne** (shins777@gmail.com)에 있습니다.