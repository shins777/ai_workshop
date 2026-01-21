# ADK 에이전트 콜백 예제 (06-callback/agent_callback)

이 예제는 에이전트의 전체 실행 수명 주기(Life Cycle) 중 에이전트 실행 전후에 특정 로직을 삽입하는 **Agent Level Callback** 패턴을 보여줍니다.

## 주요 개념

- **Agent Callback**: 에이전트가 호출되기 직전(`before_agent_callback`)과 응답을 생성한 직후(`after_agent_callback`)에 실행됩니다.
- **Workflow Control**: 콜백 내에서 특정 조건에 따라 에이전트 실행을 건너뛰거나(Skip), 즉시 사용자 지정 응답을 반환할 수 있습니다.

## 주요 구성 요소

### 1. 콜백 함수 정의 (`callback.py`)
- **`callback_before_agent`**: 에이전트 실행 전, 세션 상태(`current_state`)를 확인하여 `skip_agent` 플래그가 True이면 에이전트 호출 없이 바로 응답을 반환합니다.
- **`callback_after_agent`**: 에이전트 실행 후, 상태에 따라 응답 결과에 추가적인 알림을 포함하거나 흐름을 제어합니다.

### 2. 에이전트 정의 (`agent.py`)
- `Agent` 인스턴스 생성 시 `before_agent_callback`과 `after_agent_callback` 인자에 정의한 함수를 등록합니다.

### 3. 실행기 (`runner.py`)
- `--command` 인자를 통해 세션 상태에 플래그를 주입하고, 에이전트의 동작이 콜백에 의해 어떻게 변화하는지 확인합니다.

## 워크플로우 동작 방식
1. 사용자가 질문을 합니다.
2. 에이전트가 실행되기 전 `callback_before_agent`가 호출됩니다. 
3. 만약 `skip_agent` 플래그가 있다면, LLM을 호출하지 않고 콜백이 정의한 메시지가 반환됩니다.
4. 그렇지 않으면 LLM이 답변을 생성하고, 이후 `callback_after_agent`가 실행되어 최종 수정을 거칩니다.

## 실행 방법
`06-callback` 폴더에서 명령어를 입력하여 테스트합니다:
```bash
# 에이전트 실행 건너뛰기 테스트
uv run -m agent_callback.runner --command skip_agent

# 응답 후처리 테스트
uv run -m agent_callback.runner --command check_response
```

## 라이선스
이 프로젝트는 Apache License 2.0을 따릅니다.