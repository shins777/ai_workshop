# ADK 함수 호출 도구 예제 (03-tools/function_call)

이 예제는 일반적인 Python 함수를 에이전트가 호출할 수 있는 도구(Tool)로 등록하고 사용하는 방법을 보여줍니다.

## 주요 개념

- **Function Calling**: LLM이 질문에 답변하기 위해 외부 API 호출이나 특정 로직 실행이 필요하다고 판단하면, 등록된 Python 함수의 인자를 생성하여 호출을 요청하는 방식입니다.

## 주요 구성 요소

### 1. 함수 정의 (`function.py`)
- **`get_exchange_rate`**: Frankfurter API를 연동하여 실시간 환율을 가져오는 비즈니스 로직입니다.
- **`get_stock_price`**: Alpha Vantage API를 사용하여 주가 정보를 조회하는 로직입니다.
- **Docstring**: 함수의 역할, 인자, 반환값에 대한 상세한 독스트링은 LLM이 이 함수를 언제 어떻게 사용할지 판단하는 핵심 데이터가 됩니다.

### 2. 에이전트 정의 (`agent.py`)
- **`tools`**: 정의된 함수 리스트를 에이전트에게 제공합니다 (`tools=[function.get_exchange_rate, ...]`).
- **상세 지침**: 각 도구를 언제 사용해야 하는지, 결과 형식을 어떻게 유지해야 하는지에 대한 가이드를 포함합니다.

## 사전 준비 사항
- **STOCK_API_KEY**: 주가 조회를 위해 [Alpha Vantage](https://www.alphavantage.co/)에서 발급받은 API 키를 `.env` 파일에 설정해야 합니다.

## 실행 방법
1. `.env` 파일에 `STOCK_API_KEY`를 설정합니다.
2. `03-tools` 폴더에서 `adk web`을 실행합니다.
3. 에이전트 목록에서 `function_call`을 선택하여 다음과 같이 질문하세요:
   - "오늘 달러 대비 원화 환율이 얼마야?"
   - "구글(GOOGL) 주가 알려줘."

## 라이선스
이 프로젝트는 Apache License 2.0을 따릅니다.
