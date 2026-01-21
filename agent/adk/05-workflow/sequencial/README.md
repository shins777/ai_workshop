# ADK 순차적 워크플로우 (05-workflow/sequencial)

이 예제는 여러 에이전트를 정해진 일련의 순서대로 실행하는 **Sequential (Pipeline)** 패턴을 보여줍니다. 이전 단계의 출력 결과가 다음 단계의 입력으로 전달되어야 할 때 사용합니다.

## 주요 구성 요소

### 1. 에이전트 정의 (`agent.py`)
- **`SequentialAgent`**: 등록된 하위 에이전트들을 리스트 순서대로 실행합니다.
- **실행 순서**: `positive_critic` -> `negative_critic` -> `review_critic`

### 2. 하위 에이전트 (`sub_agent.py`)
- **`positive_critic`**: 긍정적 측면 분석 (검색 도구 활용).
- **`negative_critic`**: 부정적 측면 분석 (검색 도구 활용).
- **`review_critic`**: 앞선 두 에이전트의 결과(`positive_critic_output`, `negative_critic_output`)를 변수로 받아 최종 요약을 작성합니다.

## 워크플로우 동작 방식
1. **1단계**: `positive_critic`이 웹 검색을 통해 긍정적인 정보를 수집합니다.
2. **2단계**: `negative_critic`이 이어서 부정적인 정보를 수집합니다.
3. **3단계**: `review_critic`이 앞선 단계에서 생성된 모든 데이터를 취합하여 최종 결론을 내립니다.

## 특징
- **의존성 관리**: `SequentialAgent`는 단계별 실행을 보장하므로, 마지막 에이전트가 이전 에이전트들의 작업 결과를 활용하는 파이프라인 구조에 적합합니다.

## 실행 방법
`05-workflow` 폴더에서 `adk web`을 실행한 후, 에이전트 목록에서 `sequencial`을 선택하여 테스트할 수 있습니다.