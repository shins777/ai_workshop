# ADK 에이전트 콜백 (Agent Level Callback)

이 모듈은 에이전트의 전체 실행 수명 주기(Life Cycle) 중 에이전트 실행 전후에 특정 로직을 삽입하는 **Agent Level Callback** 패턴을 다룹니다.

에이전트 수준의 콜백은 에이전트 전체 로직이 실행되기 전(`before_agent_callback`)과 실행이 완료된 후(`after_agent_callback`)에 호출됩니다. 이를 통해 특정 조건에서 에이전트 호출 자체를 생략하거나, 최종 응답을 일괄적으로 가공할 수 있습니다.

## 주요 학습 포인트

1.  **에이전트 제어**: 특정 조건에서 LLM 호출을 생략하고 미리 정의된 응답을 즉시 반환하는 방법.
2.  **맥락 활용**: `CallbackContext`를 통해 세션 상태(`state`)를 참조하여 동적으로 흐름을 제어하는 방법.
3.  **후처리 로직**: 에이전트가 생성한 최종 결과물에 알림 메시지를 덧붙이거나 형식을 수정하는 방법.

## 프로젝트 구조

- `agent.py`: `before_agent_callback`과 `after_agent_callback`이 등록된 에이전트 정의.
- `callback.py`: 실제 전처리/후처리 로직을 담은 콜백 함수 구현.
- `run.ipynb`: 주피터 노트북 환경에서 콜백 동작을 단계별로 확인.

## 핵심 기능 설명

### 1. 에이전트 실행 전 처리 (`callback_before_agent`)
에이전트가 실행되기 직전에 호출됩니다. 이 단계에서 특정 `role`이나 `state`에 따라 에이전트 실행을 중단(Skip)시킬 수 있습니다.
- **예제**: 세션 상태에 `skip_agent=True`가 설정된 경우, LLM 호출 없이 "에이전트 호출을 건너뛰었습니다"라는 메시지를 즉시 반환합니다.

### 2. 에이전트 실행 후 처리 (`callback_after_agent`)
에이전트의 모든 로직(도구 호출 포함)이 완료된 후 최종 응답이 반환되기 직전에 호출됩니다.
- **예제**: `check_response` 플래그가 있는 경우, 에이전트의 응답을 가로채어 시스템 메시지로 대체하거나 보완합니다.

## 코드 예시

### 에이전트 등록 (`agent.py`)
```python
from callback import callback_before_agent, callback_after_agent

root_agent = Agent(
    ...,
    before_agent_callback=callback_before_agent,
    after_agent_callback=callback_after_agent 
)
```

### 콜백 로직 (`callback.py`)
```python
def callback_before_agent(callback_context: CallbackContext) -> Optional[types.Content]:
    current_state = callback_context.state.to_dict()
    if current_state.get("skip_agent"):
        # 에이전트 호출 생략 및 사용자 정의 응답 반환
        return types.Content(parts=[types.Part(text="Skip logical...")], role="model")
    return None # None 반환 시 정상 진행
```

## 활용 사례
- **권한 제어**: 특정 권한이 없는 사용자의 요청일 경우 에이전트 실행 전 차단.
- **캐싱**: 동일한 요청에 대해 미리 저장된 응답이 있는 경우 에이전트 호출 없이 즉시 반환.
- **감사 로그(Auditing)**: 에이전트의 시작과 끝 시간을 기록하거나 실행 요약을 로그로 남김.

## 라이선스
Apache License 2.0. Copyright 2025 Forusone.