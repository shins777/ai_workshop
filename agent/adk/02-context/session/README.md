# ADK 대화형 에이전트 - 세션 관리 (Session Management)

이 모듈은 ADK(에이전트 개발 키트)를 사용하여 **세션 인식형(Session-aware) 대화형 AI 에이전트**를 구축하고 관리하는 방법을 보여줍니다. 

사용자와의 대화가 단발성으로 끝나지 않고 여러 차례(Multi-turn) 이어지려면 과거의 대화 기록과 맥락을 유지해야 합니다. ADK의 세션 서비스는 이러한 대화의 연속성을 보장하기 위한 핵심 구성 요소입니다.

## 주요 학습 포인트

1.  **세션 서비스 (Session Service)**: 대화 기록과 상태를 어디에, 어떻게 저장할지 결정합니다.
2.  **멀티 턴 대화**: 이전 대화 내용을 토대로 후속 질문에 답변하는 에이전트 구성.
3.  **세션 백엔드 지원**: 테스트용 인메모리부터 운영용 데이터베이스 및 클라우드(Vertex AI) 연동까지 다양한 저장소 활용.

## 프로젝트 구조

- `agent.py`: Google 검색 도구를 갖춘 검색 기반 에이전트(`search_agent`) 정의.
- `run.ipynb`: 다양한 세션 서비스를 사용하여 에이전트를 테스트하는 인터랙티브 가이드.
- `adk_session.db`: `database` 유형 사용 시 생성되는 SQLite 데이터베이스 파일.

## 지원되는 세션 유형

| 유형 | 클래스 | 설명 | 용도 |
| :--- | :--- | :--- | :--- |
| **In-Memory** | `InMemorySessionService` | 데이터를 메모리에만 저장. 프로세스 종료 시 초기화. | 빠른 프로토타이핑, 로컬 테스트 |
| **Database** | `DatabaseSessionService` | SQLite 등 관계형 DB에 저장. 파일로 유지되므로 재시작 후에도 지속. | 중소규모 앱, 로컬 영속성 필요 시 |
| **Agent Engine** | `VertexAiSessionService` | Google Cloud Vertex AI의 Agent Engine 플랫폼에 저장. | 엔터프라이즈 환경, 클라우드 배포 |

## 환경 설정 (.env)

이 예제는 `02-context` 폴더의 상위 디렉터리에 위치한 `.env` 파일을 참조합니다.

### Vertex AI (Enterprise)
```env
GOOGLE_GENAI_USE_VERTEXAI = TRUE
GOOGLE_CLOUD_PROJECT = "YOUR_PROJECT_ID"
GOOGLE_CLOUD_LOCATION = "us-central1"
GOOGLE_GENAI_MODEL = "gemini-2.5-flash"
AGENT_ENGINE_ID = "YOUR_AGENT_ENGINE_ID"
```

### AI Studio (API Key)
```env
GOOGLE_GENAI_USE_VERTEXAI = FALSE
GOOGLE_API_KEY = "YOUR_API_KEY"
```

## 실행 가이드

### 1. 환경 인증 (GCP 사용 시)
```bash
gcloud auth application-default login
```

### 2. 세션 에이전트 실행
`uv`를 사용하여 `run.ipynb` 노트북을 열거나, 직접 코드를 작성하여 실행할 수 있습니다. 

**코드 예시 (Database 세션 사용):**
```python
from google.adk.sessions import DatabaseSessionService
from google.adk.runners import Runner
from agent import root_agent

# 1. 세션 서비스 초기화 (SQLite 사용)
db_url = "sqlite+aiosqlite:///./adk_session.db"
session_service = DatabaseSessionService(db_url=db_url)

# 2. 세션 생성 또는 가져오기
session = await session_service.create_session(
    app_name="my_app", 
    user_id="user_123"
)

# 3. 러너를 사용하여 대화 수행
runner = Runner(agent=root_agent, session_service=session_service)
events = runner.run_async(user_id="user_123", session_id=session.id, new_message="안녕?")
```

## 참고 사항
- **세션 ID 재사용**: `user_id`와 `session_id`를 동일하게 유지하면 과거 대화 기록이 자동으로 불러와집니다.
- **데이터베이스 드라이버**: 비동기 처리를 위해 `aiosqlite`를 반드시 사용해야 합니다 (`sqlite+aiosqlite:///`).

## 라이선스
Apache License 2.0. Copyright 2025 Forusone.
