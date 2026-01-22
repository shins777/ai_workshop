# ADK 대화형 에이전트 - 상태 관리 (State Management)

이 모듈은 ADK(에이전트 개발 키트)를 사용하여 **상태 기반(State-based) 대화형 에이전트**를 구축하는 방법을 보여줍니다.

단순한 대화 기록을 넘어, 에이전트가 특정 작업의 진행 상태, 사용자 선호도, 또는 시스템 변수 등 **구조화된 데이터**를 직접 수정하고 참조하는 패턴을 학습할 수 있습니다.

## 주요 학습 포인트

1.  **명시적 상태 (Explicit State)**: 세션 내에서 에이전트나 시스템이 관리하는 키-값 쌍의 데이터.
2.  **상태 델타 (State Delta)**: 이벤트를 통해 세션 상태를 부분적으로 업데이트하는 방법.
3.  **출력 키 (Output Key)**: 에이전트의 마지막 응답을 상태값으로 자동 저장하는 기능.

## 프로젝트 구조

- `agent.py`: `output_key="last_turn"` 설정이 포함된 검색 에이전트 정의.
- `runner.py`: 비동기 환경에서 이벤트를 생성하고 세션 상태를 명시적으로 업데이트하는 예제 코드.
- `run.ipynb`: 상태 관리 기능을 단계별로 확인하는 인터랙티브 가이드.

## 핵심 개념 설명

### 1. 상태 델타 (State Delta)
ADK에서 세션 상태는 직접 수정하기보다 **이벤트(Event)**를 통해 변경하는 것을 권장합니다. `EventActions`의 `state_delta`를 사용하면 현재 상태에 새로운 값을 덮어쓰거나 추가할 수 있습니다.

```python
from google.adk.events import Event, EventActions

# 상태 변경을 위한 시스템 이벤트 생성
state_changes = {"task_status": "완료", "score": 100}
system_event = Event(
    author="system",
    actions=EventActions(state_delta=state_changes)
)

# 세션에 이벤트 추가 (상태 반영)
await session_service.append_event(session, system_event)
```

### 2. 출력 키 (Output Key)
에이전트 정의 시 `output_key`를 지정하면, 해당 에이전트가 생성한 최종 응답이 세션 상태의 해당 키값으로 자동 저장됩니다.

```python
root_agent = Agent(
    name="search_agent",
    output_key="last_turn",  # 응답이 session.state['last_turn']에 저장됨
    ...
)
```

## 실행 가이드

`uv`를 사용하여 러너 스크립트를 실행합니다:

```bash
# 02-context 폴더에서 실행
uv run -m state.runner --app_name state_demo --user_id tester
```

실행 시 다음 과정을 확인할 수 있습니다:
1.  초기 세션 상태 확인.
2.  사용자 질문에 답변 후 `last_turn` 상태 업데이트 확인.
3.  시스템 이벤트를 통한 명시적 상태 변경(`task_status` 등) 확인.

## 활용 사례
- **워크플로 단계 추적**: 사용자가 현재 어떤 단계(예: 결제 중, 정보 입력 중)에 있는지 상태로 관리.
- **사용자 정보 기억**: 대화 중 추출된 정보를 상태에 저장하여 다음 턴에서 참조.
- **외부 연동**: 에이전트의 결과를 DB나 타 시스템에 전달하기 전 임시 보관.

## 라이선스
Apache License 2.0. Copyright 2025 Forusone.