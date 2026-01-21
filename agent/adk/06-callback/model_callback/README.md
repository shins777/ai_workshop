# ADK 모델 콜백 예제 (06-callback/model_callback)

이 예제는 LLM(대형 언어 모델)과 직접적으로 주고받는 메시지를 가로채어 검사하고 수정하는 **Model Level Callback** 패턴을 보여줍니다.

## 주요 개념

- **Model Callback**: 실제 LLM API 호출 직전(`before_model_callback`)과 응답 수신 직후(`after_model_callback`)에 작동합니다.
- **Content Filtering**: 사용자의 입력이나 모델의 답변에 포함된 민감한 키워드를 감지하여 차단하거나 필터링하는 정책을 구현할 때 유용합니다.

## 주요 구성 요소

### 1. 콜백 함수 정의 (`callback.py`)
- **`callback_before_model`**: `LlmRequest` 객체를 검사하여 사용자의 질문에 부적절한 키워드가 포함되어 있으면 LLM 호출을 차단하고 경고 메시지를 반환합니다.
- **`callback_after_model`**: `LlmResponse` 객체를 검사하여 생성된 답변에 금지된 단어가 포함되어 있으면 답변을 사용자에게 전달하지 않고 대체 메시지를 생성합니다.

### 2. 에이전트 정의 (`agent.py`)
- `Agent` 설정에서 `before_model_callback`과 `after_model_callback`을 등록하여 모델 통신 계층에 보안/검증 로직을 주입합니다.

### 3. 실행기 (`runner.py`)
- `--keyword`와 `--query` 인자를 통해 특정 단어 감지 로직을 실시간으로 테스트할 수 있습니다.

## 워크플로우 동작 방식
1. 에이전트가 질문을 받으면 모델 호출 단계로 진입합니다.
2. `before_model_callback`이 호출되어 질문 내용을 검사합니다.
3. 이상이 없으면 LLM이 답변을 생성합니다.
4. 생성된 답변이 사용자에게 전달되기 전 `after_model_callback`이 다시 한번 내용을 검증합니다.

## 실행 방법
`06-callback` 폴더에서 명령어를 입력하여 테스트합니다:
```bash
# 특정 키워드 감지 및 차단 테스트
uv run -m model_callback.runner --keyword 'violent' --query 'Generate some violent words'
```

## 특징
- **에이전트 로직과 분리**: 에이전트의 페르소나나 지침을 수정하지 않고도 시스템 차원의 안전장치나 모니터링 로직을 구현할 수 있습니다.

## 라이선스
이 프로젝트는 Apache License 2.0을 따릅니다.
