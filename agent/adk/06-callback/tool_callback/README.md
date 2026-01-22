# ADK 도구 콜백 (Tool Level Callback)

이 모듈은 에이전트가 도구(Tool)를 호출할 때 전달되는 인자를 수정하거나, 도구가 반환한 결과를 가공하는 **Tool Level Callback** 패턴을 다룹니다.

도구 수준의 콜백은 특정 도구가 실행되기 직전(`before_tool_callback`)과 실행이 완료된 후(`after_tool_callback`)에 호출됩니다. 모델이 도구 인자를 잘못 생성하거나 도구의 출력 형식이 사용자에게 불친절할 때, 이를 중간에서 보정하는 강력한 수단이 됩니다.

## 주요 학습 포인트

1.  **인자 보정 (Argument Mapping)**: 모델이 생성한 도구 인자가 실제 도구 사양과 미세하게 다를 때 이를 자동으로 수정하는 방법.
2.  **결과 후처리 (Result Enhancement)**: 도구가 반환한 원본 데이터에 부가 설명을 추가하거나 가독성을 높이는 방법.
3.  **동적 도구 제어**: 호출되는 도구의 이름과 인자를 실시간으로 감시하고 제어하는 방법.

## 프로젝트 구조

- `agent.py`: `get_capital_city` 도구와 콜백이 등록된 에이전트 정의.
- `callback.py`: 인자 수정을 위한 `before_tool_callback`과 결과 가공을 위한 `after_tool_callback` 구현.
- `run.ipynb`: "Korea" 입력 시 "South Korea"로 자동 보정되는 시나리오를 확인하는 노트북.

## 핵심 기능 설명

### 1. 도구 호출 전 인자 보정 (`callback_before_tool`)
도구가 실제로 실행되기 전에 호출됩니다. 모델이 넘겨준 인자(`args`)를 검사하고 수정할 수 있습니다.
- **예제**: 사용자가 "Korea"의 수도를 물어볼 때, 모델이 `country="Korea"`로 인자를 생성하면 이를 `country="south korea"`로 자동 보정하여 도구의 조회 성공률을 높입니다.

### 2. 도구 실행 후 결과 가공 (`callback_after_tool`)
도구가 실행된 후 그 결과값(`tool_response`)을 에이전트에게 전달하기 전에 호출됩니다.
- **예제**: 도구 결과가 "Seoul"인 경우, 단순한 텍스트 대신 "(Note: 이곳은 대한민국의 수도입니다)"라는 노트를 덧붙여 사용자에게 더 풍부한 정보를 제공합니다.

## 코드 예시

### 에이전트 등록 (`agent.py`)
```python
from callback import callback_before_tool, callback_after_tool, get_capital_city

root_agent = Agent(
    ...,
    tools=[get_capital_city],
    before_tool_callback=callback_before_tool,
    after_tool_callback=callback_after_tool
)
```

### 도구 인자 보정 로프 (`callback.py`)
```python
def callback_before_tool(tool: BaseTool, args: Dict[str, Any], tool_context: ToolContext) -> Optional[Dict]:
    if tool.name == 'get_capital_city' and args.get('country') == 'Korea':
        args['country'] = 'south korea' # 인자 직접 수정
    return None # None 반환 시 수정된 args로 도구 실행
```

## 활용 사례
- **포맷팅 맞춤**: 모델이 날짜 형식을 잘못 생성했을 때(예: '2025/01/01' ➔ '2025-01-01') 도구 실행 전 보정.
- **보완 정보 삽입**: 날씨 도구의 결과가 '섭씨 20도'일 때 '여행하기 좋은 날씨입니다'라는 감성적 문구 추가.
- **보안 필터링**: 도구가 반환한 SQL 쿼리 결과에서 특정 컬럼(예: 비밀번호)을 제거하여 에이전트에게 전달.

## 라이선스
Apache License 2.0. Copyright 2025 Forusone.
