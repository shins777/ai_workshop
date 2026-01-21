# ADK 대화형 에이전트 - 메모리(Memory)

이 예제는 ADK 프레임워크와 Vertex AI Agent Engine의 Memory Bank 기능을 사용하여 메모리 기능을 갖춘 대화형 AI 에이전트를 구축하고 운영하는 방법을 보여줍니다. 이 예제는 메모리 서비스를 통해 이전 세션에서 저장된 정보를 사용하여 통신하는 두 개의 에이전트로 구성됩니다. 메모리가 활성화된 대화형 에이전트는 선택된 세션 정보를 메모리에 저장하여 나중에 다른 에이전트가 해당 값을 검색할 수 있도록 합니다.

메모리 기능은 세션 전체를 데이터베이스에 저장하는 것과는 목적이 다릅니다. 메모리에 저장되는 정보는 세션의 전체 덤프가 아닌 요약된 표현입니다. 세션 데이터를 데이터베이스에 유지하는 것은 전체 세션 내용을 저장하는 반면, 메모리는 검색 및 문맥 회상을 위해 압축된 요약 정보를 저장합니다.

## .env 구성

`.env` 파일을 상위 폴더(`02-context`)에 생성하세요. 권장되는 환경 변수 및 인증 지침은 ADK 퀵스타트를 참조하세요:
https://google.github.io/adk-docs/get-started/quickstart/#set-up-the-model

아래 예제는 엔터프라이즈 환경에서 ADK를 Vertex AI / Agent Engine과 함께 실행할 때 사용되는 환경 변수를 보여줍니다. 참고: Gemini 엔드포인트 위치와 Agent Engine 위치는 독립적으로 구성할 수 있습니다.

```
GOOGLE_GENAI_USE_VERTEXAI = TRUE
GOOGLE_CLOUD_PROJECT = "YOUR_PROJECT_ID"
GOOGLE_CLOUD_LOCATION = "YOUR_PROJECT_LOCATION"
GOOGLE_GENAI_MODEL = "gemini-2.5-flash"

MEMORY_BANK_ID = "1131366489594658816"
```

AI Studio를 사용하는 개인 사용자의 경우 API 키를 다음과 같이 설정하세요:

```
GOOGLE_GENAI_USE_VERTEXAI = FALSE
GOOGLE_API_KEY = PASTE_YOUR_ACTUAL_API_KEY_HERE
```

## 예제: 데모 실행

Google Cloud로 환경 인증:

```
adk_workshop/adk/02-context$gcloud auth application-default login
```

이 예제를 테스트하려면 에이전트를 별도로 실행해야 합니다. 예제를 단계별로 실행하거나 별도의 명령어 환경에서 에이전트를 동시에 실행할 수 있습니다.

### 1. 세션을 메모리에 저장하기 위한 에이전트 실행
세션을 메모리에 추가하는 에이전트를 실행합니다.

```
adk_workshop/adk/02-context$ uv run -m memory_bank.runner_store --app_name ai_assist --user_id forus
```
"저는 Forus입니다. 당신의 이름은 무엇인가요?"와 같은 정보를 제공하세요.

### 2. 메모리에서 세션을 회상하기 위한 에이전트 실행
recall 에이전트를 사용하여 메모리에서 정보를 가져올 수 있습니다.
```
adk_workshop/adk/02-context$ uv run -m memory_bank.runner_recall --app_name ai_assist --user_id forus
```

에이전트에게 "내 이름을 기억하나요?"와 같이 이름을 물어보세요.

## 라이선스

이 프로젝트는 Apache License 2.0에 따라 라이선스가 부여됩니다. 모든 코드와 콘텐츠의 저작권은 **ForusOne** (shins777@gmail.com)에 있습니다.