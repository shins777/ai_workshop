# Google AI Workshop 종합 가이드 (Vertex AI & Gemini)

본 리포지토리는 Google Cloud Platform(GCP)의 **Vertex AI**와 최신 LLM인 **Gemini**를 활용하여 고도화된 AI 어플리케이션 및 에이전트를 구축하는 실전 워크숍 플랫폼입니다. 

기초적인 모델 호출부터 실시간 멀티모달 인터랙션, RAG 기반 지식 검색, 그리고 엔터프라이즈급 에이전트 프레임워크인 ADK(Agent Development Kit)까지 아우르는 포괄적인 예제를 제공합니다.

---

## 📂 주요 모듈 구성 및 가이드

본 워크숍은 5가지 핵심 주제로 구성되어 있습니다.

### 🤖 1. [Agent Development Kit (ADK)](./agent/adk/README.md)
엔터프라이즈급 에이전트 구축을 위한 프레임워크 활용 예제입니다.
- **Workflow**: Sequential, Parallel, Loop 등 고급 협업 패턴.
- **Context**: 세션 유지, 상태 관리, 벡터 기반 장기 기억(Memory Bank).
- **Tools**: BigQuery 연동, 코드 실행, MCP(Model Context Protocol) 기반 외부 도구 확장.

### 🌟 2. [Gemini 기초 및 도구 활용 (Gemini Basics)](./gemini/model/README.md)
Gemini 모델의 핵심 기능과 도구 활용법을 실습합니다.
- **Model Control**: 토큰 제어, 안전 설정, 구조화된 출력(JSON).
- **Multimodal**: 이미지, 비디오, 오디오 데이터 분석 및 추론.
- **Advanced Tools**: 함수 호출(Function Call), 내장 구글 검색, RAG 엔진 연동.

### 🎙️ 3. [실시간 멀티모달 인터랙션 (Live API)](./live/README.md)
Live API를 활용하여 지연 시간 없는 실시간 인텔리전스를 구현합니다.
- **Real-time API**: 저지연 음성-음성, 텍스트-음성 상호작용.
- **STT/TTS**: Cloud STT(Chirp 3.0), Gemini TTS를 활용한 고음질 음성 처리.
- **Non-native Audio**: 다양한 오디오 스트리밍 형식 처리 기법.

### 🔍 4. [RAG 및 검색 아키텍처 (RAG & Search)](./rag/README.md)
기업 내부 데이터를 지식으로 변환하고 검색하는 아키텍처를 설계합니다.
- **Embeddings**: 텍스트 및 멀티모달 임베딩 모델(Gecko 등) 활용.
- **Vector Search**: 대규모 벡터 인덱스 생성 및 의미 기반 정밀 검색(Semantic Search).

### 💻 5. [로컬 및 소형 모델 활용 (Small LLM)](./sllm/README.md)
비용 효율과 보안을 위한 소형 모델(SLLM) 운영 전략을 다룹니다.
- **Ollama**: 로컬 환경에서 Llama, Gemma 모델 구동 및 테스트.
- **Deployment**: TGI(Text Generation Inference)를 통한 모델 가속화 및 구글 클라우드 배포.

---

## 🛠️ 개발 환경 구축

본 워크숍의 모든 예제는 현대적인 Python 패키지 관리자인 `uv`를 사용합니다.

### 1. 전제 조건
- Google Cloud 프로젝트 권한 및 Vertex AI API 활성화.
- Python 3.12 이상 설치.
- [Google Cloud SDK (gcloud CLI)](https://cloud.google.com/sdk/docs/install) 설치 및 인증.

### 2. 설치 및 환경 설정
```bash
# 리포지토리 복제
git clone https://github.com/shins777/ai_workshop.git
cd ai_workshop

# uv 패키지 매니저 설치 (최초 1회)
curl -LsSf https://astral.sh/uv/install.sh | sh

# 가상 환경 및 의존성 초기화
uv sync
```

### 3. 인증 (GCP 연동 시 필수)
```bash
gcloud auth application-default login
```

---

## 🚀 실행 가이드

각 모듈은 Jupyter Notebook(`.ipynb`) 또는 Python 스크립트(`.py`)로 제공됩니다. 특히 ADK 관련 예제는 통합 UI를 지원합니다.

- **ADK 웹 테스트**: `agent/adk` 폴더로 이동 후 `adk web` 실행.
- **Jupyter Lab 시작**: `uv run jupyter lab` 명령어로 실습 노트북 실행.

## 📜 라이선스
이 프로젝트는 **Apache License 2.0**을 따릅니다. 모든 코드와 콘텐츠의 저작권은 **ForusOne**(shins777@gmail.com)에 있습니다.
