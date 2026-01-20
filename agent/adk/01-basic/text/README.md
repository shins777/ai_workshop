# ADK 기본 에이전트 예제 - ADK 핵심 개념

이 폴더는 ADK(에이전트 개발 키트) 프레임워크를 사용하여 간단한 AI 에이전트를 구축하고 실행하는 방법을 보여줍니다.

## .env 설정

`.env` 파일은 상위 폴더(`01-agent`)에 위치해야 합니다. 환경 파일에 포함할 내용에 대한 자세한 내용은 다음 URL을 참조하세요:
https://google.github.io/adk-docs/get-started/quickstart/#set-up-the-model

다음은 엔터프라이즈 환경에서 Vertex AI와 함께 ADK를 사용하기 위한 예제 구성입니다:

```
GOOGLE_GENAI_USE_VERTEXAI = TRUE
GOOGLE_CLOUD_PROJECT = "YOUR_PROJECT_ID"
GOOGLE_CLOUD_LOCATION = "YOUR_PROJECT_LOCATION"
GOOGLE_GENAI_MODEL = "gemini-2.5-flash"
```

AI Studio를 사용하는 일반 사용자의 경우 다음과 같이 GOOGLE_API_KEY를 설정하세요:

```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=PASTE_YOUR_ACTUAL_API_KEY_HERE
```

## 기본 에이전트 파일 구조
```
adk/01-agent/basic/
├── __init__.py
├── agent.py
└── README.md
```

- `agent.py`: 기본 에이전트의 빌드 및 설정 코드를 포함합니다.
- `__init__.py`: 폴더를 Python 패키지로 표시합니다.

## 예제 실행

다음 gcloud 명령어를 사용하여 Google Cloud 인증을 설정하세요:

```
gcloud auth application-default login
```

`01-agent` 폴더에서 아래 명령어를 실행하고 adk 웹 인터페이스에서 테스트하세요:

```
adk_workshop/adk/01-agent$ adk web
```

## 라이선스
이 프로젝트는 Apache License 2.0을 따릅니다. 