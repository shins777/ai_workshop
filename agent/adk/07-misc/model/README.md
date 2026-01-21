# ADK 모델 연동 전체 가이드 (07-misc/model)

이 디렉토리는 ADK(Agent Development Kit)에서 지원하는 다양한 LLM(대형 언어 모델) 연동 방식에 대한 종합적인 가이드와 설정 방법을 제공합니다. ADK는 구글의 Gemini뿐만 아니라, LiteLLM과 Ollama를 통해 외부 및 로컬의 다양한 모델을 지원합니다.

## 지원 모델 연동 방식

### 1. [LITELLM (외부 상용 모델)](../litellm/README.md)
- **대상**: OpenAI (GPT-4o), Anthropic (Claude), Mistral 등.
- **특징**: 상용 AI API를 ADK 에이전트에 즉시 통합.

### 2. [OLLAMA (로컬 설치 모델)](../ollama_agent/README.md)
- **대상**: Llama 3, Gemma, Mistral 등 로컬 PC에 설치된 모델.
- **특징**: 보안이 중요하거나 인터넷 연결 없이 에이전트를 구동해야 하는 경우 활용.

---

## 공통 환경 설정 (.env)

모든 모델 예제는 `07-misc` 폴더 내의 `.env` 파일을 참조합니다. 모델별로 필요한 환경 변수를 적절히 설정해야 합니다.

### 주요 환경 변수 예시
```env
# LiteLLM (OpenAI/Anthropic)
OPENAI_API_KEY=your_openai_key
ANTHROPIC_API_KEY=your_anthropic_key

# Ollama (Local)
OLLAMA_API_BASE=http://localhost:11434

# Google Gemini (Default)
GOOGLE_API_KEY=your_google_key
# 또는 Vertex AI 사용 시
GOOGLE_GENAI_USE_VERTEXAI=TRUE
GOOGLE_CLOUD_PROJECT=your_project_id
```

## 적합한 모델 선택 가이드

| 연동 방식 | 추천 사용 사례 | 장점 |
| :--- | :--- | :--- |
| **Gemini (Vertex AI)** | 기업용 보안 및 엔터프라이즈 앱 | 엔터프라이즈급 성능 및 GCP 통합 |
| **LiteLLM** | 다양한 글로벌 모델 비교 및 활용 | 방대한 모델 라이브러리 지원 |
| **Ollama** | 로컬 개발 및 데이터 프라이버시 | 비용 없음, 로컬 자원 활용 |

## 라이선스
이 프로젝트는 Apache License 2.0을 따릅니다.
