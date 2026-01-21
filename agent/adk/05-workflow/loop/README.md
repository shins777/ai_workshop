# ADK 루프 및 반복 개선 워크플로우 (05-workflow/loop)

이 예제는 만족스러운 결과가 나올 때까지 특정 단계를 반복하는 **Loop (Refinement)** 패턴을 보여줍니다.

## 주요 구성 요소

### 1. 에이전트 정의 (`agent.py`)
- **`LoopAgent`**: 특정 조건이 충족되거나 최대 반복 횟수(`max_iterations`)에 도달할 때까지 하위 에이전트들을 반복 실행합니다.
- **`SequentialAgent`**: 초기 조사 -> 반복 개선 루프 -> 최종 결론의 전체 파이프라인을 관리합니다.

### 2. 하위 에이전트 및 도구 (`sub_agent.py`)
- **`research_agent`**: 주제에 대한 초기 정보를 수집합니다.
- **`critic_agent`**: 결과물을 검토하고 개선 제안을 합니다. 결과가 충분히 좋으면 특정 문구(`Overall, the answer is fine.`)를 출력합니다.
- **`refine_agent`**: 비평 결과에 따라 내용을 수정하거나, 루프를 종료하는 `exit_loop` 도구를 호출합니다.
- **`exit_loop` (Tool)**: `tool_context.actions.escalate = True` 설정을 통해 루프를 탈출하고 다음 단계로 진행하도록 신호를 보냅니다.
- **`conclusion_agent`**: 최종 개선된 내용을 바탕으로 요약을 작성합니다.

## 워크플로우 동작 방식
1. `research_agent`가 초안을 작성합니다.
2. **반복 루프 시작**:
    - `critic_agent`가 초안을 비평합니다.
    - 내용이 부족하면 `refine_agent`가 수정안을 작성하고 다시 비평 단계로 돌아갑니다.
    - 내용이 만족스러우면 `refine_agent`가 `exit_loop`를 호출하여 루프를 빠져나옵니다.
3. `conclusion_agent`가 최종본을 출력합니다.

## 실행 방법
`05-workflow` 폴더에서 `adk web`을 실행한 후, 에이전트 목록에서 `loop`을 선택하여 테스트할 수 있습니다.