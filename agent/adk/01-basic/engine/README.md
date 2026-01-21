# ADK Agent Engine 배포 및 실행 (01-basic)

이 폴더는 ADK 에이전트를 **Vertex AI Agent Engine**에 배포하고 관리하는 전 과정을 담고 있습니다. 제공되는 `run.ipynb` 노트북을 통해 에이전트 빌드, 배포, 업데이트, 그리고 SDK 및 REST API를 이용한 질의를 단계별로 수행할 수 있습니다.

## 주요 구성 파일

- **`agent.py`**: ADK `Agent` 클래스를 사용하여 실제 에이전트의 로직(이름, 모델, 지침, 도구 등)을 정의합니다.
- **`run.ipynb`**: 에이전트의 라이프사이클(초기화 → 빌드 → 배포/업데이트 → 실행)을 관리하는 대화형 노트북입니다.

## 사전 준비 사항

### 1. 환경 변수 설정
상위 폴더(`01-basic`)에 위치한 `.env` 파일에 다음 항목들이 올바르게 설정되어 있어야 합니다:
```bash
GOOGLE_GENAI_USE_VERTEXAI=TRUE
GOOGLE_CLOUD_PROJECT="발급받은-프로젝트-ID"
GOOGLE_CLOUD_LOCATION="us-central1" # 또는 다른 지원 지역
GOOGLE_GENAI_MODEL="gemini-2.0-flash-exp" # 사용할 모델 명
AGENT_ENGINE_BUCKET="gs://에이전트-배포용-GCS-버킷-이름"
```

### 2. Google Cloud 인증
터미널에서 다음 명령어를 실행하여 인증을 완료합니다:
```bash
gcloud auth application-default login
```

## 단계별 실행 가이드 (`run.ipynb`)

`run.ipynb`는 다음과 같은 단계로 구성되어 있습니다:

### Step 1: 환경 초기화 및 에이전트 빌드
- **환경 로드**: `.env` 파일에서 프로젝트 설정 및 GCS 버킷 정보를 읽어옵니다.
- **Vertex AI 초기화**: 배포 대상 프로젝트와 위치, 스테이징 버킷을 설정합니다.
- **`AdkApp` 생성**: `agent.py`에서 정의한 에이전트를 Agent Engine 형식으로 패키징합니다.

### Step 2: 에이전트 배포 또는 업데이트
- **Deploy (`create = True`)**: 에이전트를 처음 배포할 때 사용합니다. 성공 시 고유한 `resource_name`이 생성됩니다.
- **Update (`create = False`)**: 이미 배포된 에이전트의 로직(수정된 `agent.py` 등)을 업데이트할 때 사용합니다. `agent_engine_resource_name` 변수에 기존 리소스 이름을 입력해야 합니다.

### Step 3: 에이전트 실행 (Python SDK)
- `remote_agent.async_create_session()`을 통해 대화 세션을 생성합니다.
- `remote_agent.async_stream_query()`를 사용하여 실시간 스트리밍 방식으로 에이전트와 대화합니다.
    - **참고**: 원격 에이전트는 비동기(async) 방식으로 동작하므로 `async for` 루프를 사용해야 이벤트 내용을 정상적으로 확인할 수 있습니다.

### Step 4: 에이전트 실행 (REST API)
- Python의 `requests` 라이브러리 또는 `curl` 명령어를 사용하여 HTTP POST 요청으로 에이전트에 질의하는 방법을 보여줍니다.
- 이 방식은 다른 애플리케이션에서 배포된 에이전트를 호출할 때 유용합니다.

## 주의 사항
- **지역(Location)**: Vertex AI Agent Engine은 현재 특정 지역(예: `us-central1`)에서만 안정적으로 지원됩니다. 설정한 지역이 지원되는지 확인하세요.
- **비동기 처리**: 노트북 내에서 에이전트를 직접 호출할 때는 반드시 `await`와 비동기 이터레이터를 사용해야 응답 메시지를 올바르게 수신할 수 있습니다.

## 라이선스
이 프로젝트는 Apache License 2.0을 따릅니다. 
