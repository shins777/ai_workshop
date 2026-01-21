# ADK 기본 에이전트 예제 통합 가이드 (01-basic)

이 디렉토리는 ADK(Agent Development Kit) 프레임워크의 핵심 개념을 단계별로 학습할 수 있는 네 가지 주요 예제를 포함하고 있습니다. 각 예제는 기본 텍스트 검색부터 실시간 멀티모달 통신, 멀티 에이전트 협업, 그리고 클라우드 배포까지의 과정을 다룹니다.

## 예제 디렉토리 구성 및 목적

### 1. [TEXT (텍스트 기반 검색 에이전트)](./text/README.md)
- **목적**: 가장 기본적인 텍스트 기반 에이전트 구성과 도구(Tool) 사용법을 학습합니다.
- **주요 내용**: `google_search` 도구를 에이전트에 내장하여, 모델의 학습 데이터에 없는 최신 정보를 실시간 웹 검색을 통해 답변하는 방법을 보여줍니다.

### 2. [LIVE (멀티모달 실시간 에이전트)](./live/README.md)
- **목적**: Gemini Multimodal Live API를 사용하여 오디오/비디오 기반의 대화형 에이전트를 구축합니다.
- **주요 내용**: 실시간 저지연 상호작용을 위한 설정 방법과 비디오/오디오 스트리밍 처리를 위한 SSL 인증서 설정 등 기술적 요구사항을 다룹니다.

### 3. [RUNNER (멀티 에이전트 시스템)](./runner/README.md)
- **목적**: 상위 에이전트(Root Agent)와 하위 에이전트(Sub-Agents) 간의 계층 구조 및 협업 로직을 학습합니다.
- **주요 내용**: 사용자의 질문 의도에 따라 루트 에이전트가 긍정적인 리뷰 에이전트(`positive_critic`) 또는 부정적인 리뷰 에이전트(`negative_critic`)를 선택적으로 호출하는 워크플로우를 구현합니다.

### 4. [ENGINE (Vertex AI 클라우드 배포)](./engine/README.md)
- **목적**: 로컬에서 개발한 에이전트를 구글 클라우드인 **Vertex AI Agent Engine** 인프라에 배포하고 관리합니다.
- **주요 내용**: `run.ipynb` 노트북을 통해 에이전트의 라이프사이클(빌드 → 배포 → 업데이트)을 관리하며, 배포된 원격 에이전트를 SDK 및 REST API로 호출하는 방법을 설명합니다.

---

## 공통 사전 준비 사항

### 1. 환경 변수 설정 (`.env`)
`01-basic` 폴더 내에 `.env` 파일을 생성하고 다음 필수 항목을 설정합니다:
```bash
GOOGLE_GENAI_USE_VERTEXAI=TRUE
GOOGLE_CLOUD_PROJECT="발급받은-프로젝트-ID"
GOOGLE_CLOUD_LOCATION="us-central1"
GOOGLE_GENAI_MODEL="gemini-2.0-flash-exp"
GOOGLE_GENAI_LIVE_MODEL="gemini-2.0-flash-exp"
AGENT_ENGINE_BUCKET="gs://에이전트-배포용-GCS-버킷-이름"
```

### 2. 인증 및 도구 설치
- **Python 환경**: `uv` 또는 `pip`를 사용하여 필요한 패키지(`google-adk`, `google-cloud-aiplatform` 등)를 설치합니다.
- **GCP 인증**: 터미널에서 `gcloud auth application-default login`을 실행합니다.

## 실행 방법 요약

모든 예제는 ADK 통합 웹 인터페이스인 `adk web`을 통해 통합 테스트가 가능합니다.

1. `01-basic` 폴더에서 명령어를 실행합니다:
   ```bash
   adk web
   ```
2. 웹 UI에서 테스트하고자 하는 에이전트(`text`, `live`, `runner` 등)를 선택하여 상호작용합니다.
3. 배포와 관련된 상세 테스트는 `engine` 폴더의 `run.ipynb`를 이용하세요.

## 라이선스
이 프로젝트는 Apache License 2.0을 따릅니다.