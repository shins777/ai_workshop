# ADK 에이전트 런타임 및 배포 예제

## 예제 개요
이 폴더는 ADK(Agent Development Kit)를 사용하여 기본적인 AI 에이전트를 정의하고, 이를 Vertex AI Agent Engine에 배포하고, 원격에서 실행하는 전체 과정을 보여줍니다.

이 예제는 다음 파일들로 구성됩니다.
- `agent.py`: 기본적인 `basic_agent`를 정의합니다. Google Search 도구를 포함합니다.
- `deploy.py`: 정의된 에이전트를 Vertex AI Agent Engine에 배포하는 스크립트입니다.
- `run.py`: 배포된 원격 Agent Engine 인스턴스에 접속하여 쿼리를 실행하는 스크립트입니다.

## .env 환경 설정

상위 폴더(`01-basic/`)에 `.env` 파일을 생성하고 필요한 환경 변수를 설정해야 합니다. 자세한 내용은 ADK 퀵스타트를 참조하세요.

https://google.github.io/adk-docs/get-started/quickstart/#set-up-the-model

예시 (`.env`):

```bash
GOOGLE_GENAI_USE_VERTEXAI=TRUE
GOOGLE_CLOUD_PROJECT="YOUR_PROJECT_ID"
GOOGLE_CLOUD_LOCATION="us-central1"
GOOGLE_GENAI_MODEL="gemini-2.5-flash"

AGENT_ENGINE_BUCKET="gs://your-bucket-name" # 배포 아티팩트 저장용 GCS 버킷
```

## 실행 방법

모든 명령어는 `01-basic` 디렉토리(이 폴더의 상위 폴더)에서 실행하는 것을 가정합니다.

### 1. Google Cloud 인증

```bash
gcloud auth application-default login
```

### 2. 에이전트 배포 (Deploy)

`deploy.py`를 실행하여 에이전트를 Vertex AI Agent Engine에 배포합니다.

```bash
uv run -m engine.deploy --agent_name 'engine_0120'
```

배포가 성공하면 Agent Engine ID 또는 리소스 이름이 출력됩니다. 이를 다음 단계에서 사용합니다.

### 3. 원격 에이전트 실행 (Run)

배포된 Agent Engine ID를 사용하여 원격으로 질의를 수행합니다.

```bash
uv run -m engine.run --engine_id <ENGINE_ID> --user_id test_user --query '생성형 AI란 무엇인가요?'
```

### 4. 코드 설명
- **agent.py**: `Agent` 클래스를 사용하여 `basic_agent`를 생성합니다. `INSTRUCTION`에 한국어 프롬프트가 설정되어 있습니다.
- **deploy.py**: `AdkApp`과 `vertexai` 라이브러리를 사용하여 로컬 에이전트 객체를 원격 인프라(Agent Engine)에 배포합니다.
- **run.py**: 배포된 리소스를 `get_agent_engine`으로 가져와 `stream_query`를 통해 대화를 나눕니다.

## 라이선스
이 프로젝트는 Apache License 2.0을 따르며, 모든 코드와 콘텐츠의 저작권은 **ForusOne**(shins777@gmail.com)에 있습니다.
