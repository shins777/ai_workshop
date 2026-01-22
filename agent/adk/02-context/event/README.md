# ADK 대화형 에이전트 - 이벤트 시스템 (Event System)

이 모듈은 ADK(에이전트 개발 키트) 프레임워크의 핵심인 **이벤트 기반 통신** 구조를 깊이 있게 이해하고 활용하는 방법을 보여줍니다.

ADK에서 에이전트와 사용자의 모든 상호작용은 '이벤트(Event)'라는 단위로 처리됩니다. 이벤트를 직접 핸들링하면 에이전트의 사고 과정, 도구 호출, 최종 응답 생성 등 모든 단계를 세밀하게 모니터링하고 제어할 수 있습니다.

## 주요 학습 포인트

1.  **이벤트 스트리밍**: 에이전트의 응답이 실시간으로 생성되는 과정을 이벤트 단위로 수신.
2.  **이벤트 구조 분석**: `invocation_id`, `author`, `actions` 등 이벤트 객체의 주요 필드 이해.
3.  **근거(Grounding) 데이터 확인**: Google 검색 등 도구 사용 시 참조된 소스(URI, 도메인 등)를 이벤트에서 추출.

## 프로젝트 구조

- `agent.py`: Google 검색 도구를 활용하는 검색 에이전트 정의.
- `run.ipynb`: `Runner`를 통해 이벤트를 비동기 스트림으로 받고, 각 이벤트의 내부 데이터를 파싱하여 출력하는 예제.

## 핵심 개념 설명

### 1. 이벤트의 구성 요소
`Runner.run_async()` 또는 `run_sync()`를 통해 반환되는 이벤트는 다음과 같은 정보를 포함합니다.

- `id`: 개별 이벤트의 고유 식별자.
- `invocation_id`: 단일 요청-응답 쌍(Invocation)을 묶는 식별자.
- `author`: 이벤트를 생성한 주체 (`user`, `agent`, `tool`, `system`).
- `actions`: 상태 변경(`state_delta`), 도구 실행 요청 등을 담은 객체.
- `content`: 텍스트 응답 등 실제 메시지 내용.
- `grounding_metadata`: 답변의 근거가 되는 참조 데이터 (URI, 제목 등).

### 2. 이벤트 스트 처리 예시 (Python)

```python
async for event in runner.run_async(...):
    print(f"작성자: {event.author}")
    
    # 최종 응답인 경우만 출력
    if event.is_final_response():
        print(f"최종 답변: {event.content.parts[0].text}")
        
    # 근거 정보가 있는 경우 출력
    if event.grounding_metadata:
        for chunk in event.grounding_metadata.grounding_chunks:
            print(f"참조: {chunk.web.title} ({chunk.web.uri})")
```

## 실행 가이드

`uv`를 사용하여 `run.ipynb` 노트북을 열어 실행하거나, `adk web`을 통해 시각적으로 확인해 보세요.

### 시각적 분석 (추천)
ADK 웹 도구를 사용하면 코드 작성 없이도 이벤트가 어떻게 발생하고 전달되는지 한눈에 볼 수 있습니다.

```bash
# 02-context 폴더에서 실행
adk web
```

## 활용 사례
- **진행 상태 표시**: 에이전트가 생각 중이거나 도구를 호출할 때 사용자에게 UI로 상태 전달.
- **도구 실행 승인**: 도구 호출 이벤트가 발생했을 때 사용자에게 승인 여부를 묻는 워크플로 구현.
- **디버깅**: 에이전트가 왜 특정 답변을 내놓았는지 단계별 이벤트 로그를 통해 분석.

## 라이선스
Apache License 2.0. Copyright 2025 Forusone.