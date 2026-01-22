# ADK 대화형 에이전트 - 장기 메모리 (Long-term Memory)

이 모듈은 ADK(에이전트 개발 키트)와 Vertex AI의 **Memory Bank** 기능을 사용하여 에이전트에게 **장기 기억(Long-term Memory)**을 부여하는 방법을 보여줍니다.

일반적인 세션 관리가 단일 대화의 흐름을 유지한다면, 메모리 서비스는 **서로 다른 세션, 심지어 서로 다른 에이전트 간에도** 중요한 정보를 공유하고 회상할 수 있게 해줍니다.

## 주요 학습 포인트

1.  **메모리 뱅크 (Memory Bank)**: 정보를 벡터화하여 저장하고 검색할 수 있는 장기 저장소.
2.  **메모리 서비스 (Memory Service)**: 세션 데이터를 요약하여 메모리 뱅크에 저장하거나 검색하는 인터페이스.
3.  **메모리 도구 (Memory Tool)**: 에이전트가 대화 중에 직접 메모리를 검색할 수 있도록 해주는 `PreloadMemoryTool`.

## 프로젝트 구조

- `agent.py`: 메모리를 저장하는 에이전트(`search_agent`)와 메모리를 회상하는 에이전트(`recall_agent`) 정의.
- `run.ipynb`: 메모리 뱅크용 에이전트 엔진을 생성하고, 데이터를 저장 및 검색하는 전 과정을 담은 가이드.

## 핵심 개념 설명

### 1. 세션 유지 vs 장기 메모리
- **Session**: 대화 전체 내용을 DB에 저장. (과거 대화 문맥 유지 목적)
- **Memory**: 대화 내용 중 핵심 사실(Fact)을 추출하여 요약 저장. (세션 간 지식 공유 및 빠른 회상 목적)

### 2. Vertex AI Memory Bank 연동
ADK의 `VertexAiMemoryBankService`를 사용하면 Google Cloud의 백엔드 인프라를 통해 안전하게 메모리를 관리할 수 있습니다.

### 3. PreloadMemoryTool
에이전트가 대화 중에 "지난번에 내가 말한 내 이름이 뭐야?"와 같은 질문을 받았을 때, 이 도구를 사용하여 메모리 뱅크에서 관련 정보를 자동으로 찾아냅니다.

```python
from google.adk.tools import preload_memory_tool

recall_agent = Agent(
    ...
    tools=[preload_memory_tool.PreloadMemoryTool()],
)
```

## 실행 가이드

### 1. 에이전트 엔진 생성
메모리 뱅크를 사용하려면 먼저 Vertex AI에 에이전트 엔진을 배포해야 합니다. `run.ipynb`의 초기 셀을 실행하여 `agent_engine_id`를 확보하세요.

### 2. 메모리 저장 (Store)
`search_agent`를 통해 대화를 나눈 후, 해당 세션을 메모리에 추가합니다.
```python
await memory_service.add_session_to_memory(completed_session)
```

### 3. 메모리 회상 (Recall)
`recall_agent`를 실행하여 이전 세션에서 저장된 정보를 물어보세요.
```python
# 예: "내 이름이 뭔지 기억해?"
async for event in recall_runner.run_async(...):
    ...
```

## 환경 설정 (.env)
```env
GOOGLE_GENAI_USE_VERTEXAI = TRUE
GOOGLE_CLOUD_PROJECT = "YOUR_PROJECT_ID"
GOOGLE_CLOUD_LOCATION = "us-central1"
# 에이전트 엔진 생성 후 획득한 ID 입력
MEMORY_BANK_ID = "YOUR_MEMORY_BANK_ID"
```

## 라이선스
Apache License 2.0. Copyright 2025 Forusone.