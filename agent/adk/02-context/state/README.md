# ADK 대화형 에이전트 - 상태(State)

## 예제 개요
이 폴더는 ADK(에이전트 개발 키트)를 사용하여 상태 기반 대화형 에이전트를 구축하는 방법을 보여줍니다. 고급 문맥 처리 및 흐름 제어를 가능하게 하기 위해 세션 상태를 수정하고 활용하는 방법을 보여줍니다. 이 예제는 세션 상태가 세션 내에서 어떻게 변경되고 활용될 수 있는지 보여줍니다.

## .env 구성

`.env` 파일을 상위 폴더(`02-context`)에 배치하세요. 환경 변수 및 인증 단계는 ADK 퀵스타트를 참조하세요:
https://google.github.io/adk-docs/get-started/quickstart/#set-up-the-model

다음 환경 설정은 엔터프라이즈 환경에서 Vertex AI와 함께 ADK를 사용하기 위한 예시입니다:

```
GOOGLE_GENAI_USE_VERTEXAI = TRUE
GOOGLE_CLOUD_PROJECT = "YOUR_PROJECT_ID"
GOOGLE_CLOUD_LOCATION = "YOUR_PROJECT_LOCATION"
GOOGLE_GENAI_MODEL = "gemini-2.5-flash"
```

AI Studio를 사용하는 개인 사용자의 경우 API 키를 다음과 같이 설정하세요:

```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=PASTE_YOUR_ACTUAL_API_KEY_HERE
```

## 소스 코드 실행 방법

Google Cloud로 환경 인증:

```bash
adk_workshop/adk/02-context$ gcloud auth application-default login
```

`output_key`는 세션에서 지난 턴 출력의 간단하고 쉽게 접근할 수 있는 지표를 저장하는 데 사용되는 예약어입니다. 멀티 턴 환경에서 이는 가장 최근 턴의 최종 출력에 대한 정보를 보유합니다.

세션 상태는 일반적으로 상태 델타(state delta)를 포함하는 이벤트를 추가하여 변경됩니다. 예를 들면 다음과 같습니다:

```python
await session_service.append_event(session, system_event)
```

다음 명령으로 예제 실행:

```bash
adk_workshop/adk/02-context$ uv run -m state.runner --app_name ai_assist --user_id forus
```

## 라이선스

이 프로젝트는 Apache License 2.0에 따라 라이선스가 부여됩니다. 모든 코드와 콘텐츠의 저작권은 **ForusOne** (shins777@gmail.com)에 있습니다.