# ADK 대화형 에이전트 - 세션(Session)

이 폴더는 ADK(에이전트 개발 키트)를 사용하여 세션 인식형 대화형 AI 에이전트를 구축하고 운영하는 방법을 보여줍니다. 이 예제는 Google 검색을 사용하여 질문에 답변하는 동안 다중 사용자 상호작용 전반에 걸쳐 세션 상태를 유지하는 방법을 보여줍니다.

세션 대화 에이전트의 주요 기능:
- 내부 기술 자료와 실시간 Google 검색 결과를 모두 사용하여 사용자 질문에 답변
- 여러 턴에 걸쳐 세션 상태 및 이벤트 기록 유지
- 다양한 세션 백엔드 지원: 인메모리(in-memory), SQLite(데이터베이스), Agent Engine(Vertex AI)
- 각 턴 이후 상세 세션 속성 및 이벤트 출력

## .env 구성

`.env` 파일을 상위 폴더(`02-context`)에 생성하세요. 권장되는 환경 변수 및 인증 지침은 ADK 퀵스타트를 참조하세요:
https://google.github.io/adk-docs/get-started/quickstart/#set-up-the-model

아래 예제는 엔터프라이즈 환경에서 ADK를 Vertex AI / Agent Engine과 함께 실행할 때 사용되는 환경 변수를 보여줍니다. 참고: Gemini 엔드포인트 위치와 Agent Engine 위치는 독립적으로 구성할 수 있습니다.

```
GOOGLE_GENAI_USE_VERTEXAI = TRUE
GOOGLE_CLOUD_PROJECT = "YOUR_PROJECT_ID"
GOOGLE_CLOUD_LOCATION = "YOUR_PROJECT_LOCATION"
GOOGLE_GENAI_MODEL = "gemini-2.5-flash"

AGENT_ENGINE_ID = "YOUR_AGENT_ENGINE_ID"
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

지원되는 세션 백엔드 중 하나로 세션 에이전트를 실행하세요:

```
adk_workshop/adk/02-context$ uv run -m session.runner --type <session_type> --app_name <app_name> --user_id <user_id> --session_id <session_id>
```

사용 가능한 세션 유형: `in_memory`, `database`, `agent_engine`

서버는 첫 실행 시 자동으로 세션을 생성합니다. 세션이 존재하는 동안 후속 상호작용은 대화 기록 및 세션 상태를 참조할 수 있습니다. `database` 또는 `agent_engine`을 사용할 때 동일한 앱 이름, 사용자 ID 및 세션 ID를 재사용하는 한 세션 데이터는 프로세스 재시작 시에도 유지됩니다.

### 1) 인메모리(in_memory) 세션 유형

이 모드는 세션을 메모리에만 저장합니다. 프로세스가 종료되면 모든 세션 데이터가 손실됩니다. 빠른 로컬 테스트에 이 모드를 사용하세요.

예제:

```
adk_workshop/adk/02-context$ uv run -m session.runner --type in_memory --app_name ai_assist --user_id forus --session_id forus_sess_001
```

### 2) 데이터베이스(database) 세션 유형

이 모드는 세션을 관계형 데이터베이스(예제는 SQLite 사용)에 유지합니다. 세션 상태는 프로세스 재시작 후에도 유지됩니다.

예제:

```
adk_workshop/adk/02-context$ uv run -m session.runner --type database --app_name ai_assist --user_id forus --session_id forus_sess_001
```

SQLite를 사용하는 경우 파일(예: `adk_database.db`)이 생성됩니다. SQLite 뷰어 또는 VS Code 확장을 사용하여 검사할 수 있습니다.

### 3) Agent Engine (Vertex AI) 세션 유형

이 모드는 세션을 Vertex AI Agent Engine 인스턴스에 저장합니다. Agent Engine은 에이전트와 해당 세션을 호스팅하도록 설계된 별도로 배포된 서비스(예: Cloud Run)입니다. 이 모드를 사용하려면 Agent Engine을 생성하고 `.env` 파일에 ID를 설정하세요:

```
AGENT_ENGINE_ID = "1769934533233804800"
```

실행 명령 예제:

```
adk_workshop/adk/02-context$ uv run -m session.runner --type agent_engine --app_name ai_assist --user_id forus --session_id forus_sess_001
```

VertexAiSessionService 사용 시 참고 사항 (2025년 8월 기준, google-adk==1.12.0):
- VertexAiSessionService는 세션 ID를 기반으로 세션 생성을 지원합니다.
- 세션은 `app_name`, `user_id`, `session_id`를 사용하여 쿼리하고 재개할 수 있습니다.
- 세션 ID가 제공되지 않으면 예제에서 자동으로 생성됩니다.

## 라이선스

이 프로젝트는 Apache License 2.0에 따라 라이선스가 부여됩니다. 모든 코드와 콘텐츠의 저작권은 **ForusOne** (shins777@gmail.com)에 있습니다.
