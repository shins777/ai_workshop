# ADK LiteLLM 다중 모델 예제 (07-misc/litellm)

이 예제는 ADK에서 **LiteLLM** 라이브러리를 통해 Google Gemini 외에도 OpenAI, Anthropic 등 다양한 외부 LLM 제공자를 손쉽게 연동하여 사용하는 방법을 보여줍니다.

## 주요 개념

- **LiteLLM**: 서로 다른 LLM 제공자(OpenAI, Anthropic, Mistral 등)의 API 형식을 하나로 통합해주는 프록시 라이브러리입니다.
- **LlmAgent**: ADK의 `LlmAgent` 클래스는 LiteLLM 모델 객체를 인자로 받아 멀티 모델 에이전트를 생성할 수 있게 해줍니다.

## 주요 구성 요소

### 1. 모델 연동 로직 (`llm.py`)
- **`LiteLlm(model="...")`**: LiteLLM에서 정의한 모델 식별자(예: `openai/gpt-4o`, `anthropic/claude-3-haiku-20240307`)를 사용하여 모델 인스턴스를 생성합니다.
- **`build_agent`**: 사용자가 원하는 모델 유형(gpt, claude)에 따라 적절한 에이전트 설정을 반환하는 팩토리 함수입니다.

## 사전 준비 사항

`.env` 파일에 각 제공자의 API 키를 설정해야 합니다:
```env
OPENAI_API_KEY=your_openai_key
ANTHROPIC_API_KEY=your_anthropic_key
```

## 실행 방법

1. `07-misc` 폴더에서 `adk web`을 실행합니다.
2. `litellm` 에이전트를 선택하여 테스트합니다.
3. 기본적으로 예제는 `gpt-4o`를 사용하도록 설정되어 있으며, 필요에 따라 `llm.py`의 `build_agent("claude")` 호출로 변경하여 테스트할 수 있습니다.

## 활용 사례
- 특정 작업에 더 적합한 모델(예: 코딩은 GPT, 추론은 Claude)을 선택적으로 사용하고 싶을 때.
- 여러 모델의 답변 품질을 같은 ADK 환경에서 비교 테스트하고 싶을 때.

## 라이선스
이 프로젝트는 Apache License 2.0을 따릅니다.
