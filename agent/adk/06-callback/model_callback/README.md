# ADK 모델 콜백 (Model Level Callback)

이 모듈은 LLM(대형 언어 모델)과 주고받는 메시지(Request/Response)를 직접 가로채어 검사하고 수정하는 **Model Level Callback** 패턴을 다룹니다.

모델 수준의 콜백은 실제 LLM API가 호출되기 직전(`before_model_callback`)과 모델로부터 응답을 수신한 직후(`after_model_callback`)에 작동합니다. 이를 통해 민감한 정보를 필터링하거나, 답변의 품질을 강제로 조정하는 가드레일(Guardrail)을 구현할 수 있습니다.

## 주요 학습 포인트

1.  **LlmRequest 제어**: 모델에 전달되는 프롬프트를 검사하여 부적절한 요청을 사전 차단하는 방법.
2.  **LlmResponse 제어**: 모델이 생성한 답변에 특정 금지어 등이 포함된 경우 답변을 수정하거나 차단하는 방법.
3.  **동적 가드레일**: 세션 상태에 따라 감시할 키워드를 동적으로 변경하여 적용하는 방법.

## 프로젝트 구조

- `agent.py`: `before_model_callback`과 `after_model_callback`이 등록된 에이전트 정의.
- `callback.py`: `LlmRequest`와 `LlmResponse` 객체를 다루는 콜백 함수 구현.
- `run.ipynb`: 특정 키워드 차단 시나리오를 테스트하는 인터랙티브 가이드.

## 핵심 기능 설명

### 1. 모델 호출 전 검사 (`callback_before_model`)
LLM API로 요청이 나가기 전에 호출됩니다. 사용자의 입력(`LlmRequest`)에 부적절한 내용이 있는지 검사합니다.
- **예제**: `keyword`가 포함된 질문이 들어오면 LLM을 호출하지 않고 "차단되었습니다"라는 내용의 `LlmResponse`를 즉시 반환하여 API 비용을 절감하고 보안을 유지합니다.

### 2. 모델 응답 후 검사 (`callback_after_model`)
모델이 답변을 생성한 직후(`LlmResponse`) 호출됩니다. 생성된 답변이 정책에 위반되는지 검사합니다.
- **예제**: 답변 내에 금지된 단어가 발견되면, 원래 답변을 사용자에게 보여주지 않고 "정책 위반으로 응답이 차단되었습니다"라는 대체 메시지로 교체합니다.

## 코드 예시

### 에이전트 등록 (`agent.py`)
```python
from callback import callback_before_model, callback_after_model

root_agent = Agent(
    ...,
    before_model_callback=callback_before_model,
    after_model_callback=callback_after_model 
)
```

### 모델 요청 차단 로직 (`callback.py`)
```python
def callback_before_model(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    keyword = callback_context.state.get("keyword")
    user_input = llm_request.contents[-1].parts[0].text
    
    if keyword in user_input:
        return LlmResponse(content=types.Content(parts=[types.Part(text="Blocked!")], role="model"))
    return None
```

## 활용 사례
- **가드레일(Safety)**: 폭력적, 혐오적 표현이 포함된 질문이나 답변을 실시간으로 차단.
- **PII 마스킹**: 실명을 포함한 개인정보가 모델에 전달되거나 답변에 포함되는 것을 방지.
- **포맷 강제**: 모델의 답변이 특정 형식을 따르지 않을 경우 콜백에서 형식을 보정하여 반환.

## 라이선스
Apache License 2.0. Copyright 2025 Forusone.
