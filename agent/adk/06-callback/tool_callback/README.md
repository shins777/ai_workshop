# ADK 도구 콜백 예제 (06-callback/tool_callback)

이 예제는 에이전트가 도구(Tool)를 호출할 때 전달되는 인자를 수정하거나, 도구가 반환한 결과를 가공하는 **Tool Level Callback** 패턴을 보여줍니다.

## 주요 개념

- **Tool Callback**: 특정 도구가 실행되기 직전(`before_tool_callback`)과 실행 완료 후(`after_tool_callback`)에 호출됩니다.
- **Dynamic Parameter Adjustment**: 사용자 질문을 도구 인자로 변환하는 과정에서 발생할 수 있는 오류를 보정하거나, 도구의 원본 출력에 부가 정보를 더할 때 사용합니다.

## 주요 구성 요소

### 1. 도구 및 콜백 정의 (`callback.py`)
- **`get_capital_city`**: 국가명을 입력받아 수도를 알려주는 간단한 도구 함수입니다.
- **`callback_before_tool`**: 도구 호출 전 인자를 확인하여 'Korea'를 'South Korea'로 자동 보정하여 도구가 정확한 정보를 찾도록 돕습니다.
- **`callback_after_tool`**: 도구 결과가 'Seoul'인 경우 "대한민국의 수도"라는 추가적인 노트를 덧붙여 사용자에게 더 풍부한 정보를 제공합니다.

### 2. 에이전트 정의 (`agent.py`)
- 에이전트가 도구를 사용할 때 `before_tool_callback`과 `after_tool_callback`이 작동하도록 설정합니다.

## 워크플로우 동작 방식
1. 사용자가 "Korea의 수도가 어디야?"라고 묻습니다.
2. 에이전트가 `get_capital_city(country='Korea')` 호출을 시도합니다.
3. `callback_before_tool`이 실행되어 인자를 `South Korea`로 변경합니다.
4. 도구가 실행되어 `Seoul`을 반환합니다.
5. `callback_after_tool`이 실행되어 결과에 부연 설명을 추가합니다.

## 실행 방법
`06-callback` 폴더에서 명령어를 입력하여 테스트합니다:
```bash
# 도구 인자 보정 및 결과 가공 테스트
uv run -m tool_callback.runner --query 'What is the capital city of Korea?'
```

## 활용 사례
- 레거시 API의 입력 형식을 에이전트가 잘 생성하지 못할 때 중간에서 보정.
- 도구가 반환한 원본 데이터에서 민감한 정보 마스킹.
- 도구 응답의 품질을 검증하고 필요한 경우 재시도 로직 삽입.

## 라이선스
이 프로젝트는 Apache License 2.0을 따릅니다.
