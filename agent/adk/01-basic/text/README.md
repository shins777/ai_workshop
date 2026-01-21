# ADK 텍스트 웹 검색 에이전트 예제 (01-basic/text)

이 폴더는 ADK(에이전트 개발 키트)를 사용하여 **Google Search 도구**를 활용하는 기본적인 텍스트 기반 에이전트를 구축하는 방법을 보여줍니다. 사용자가 질문을 하면 에이전트가 필요에 따라 웹 검색을 수행하여 최신 정보를 바탕으로 답변합니다.

## 주요 특징

- **도구 활용 (Tool Use)**: `google_search` 도구를 내장하여 에이전트가 실시간 웹 검색을 수행할 수 있습니다.
- **간결하고 명확한 응답**: 페르소나 설정을 통해 질문에 대한 이해도를 설명하고 명확한 답변을 제공하도록 설계되었습니다.

## 구성 파일 설명

- **`agent.py`**: Google Search 도구를 사용하는 에이전트를 정의합니다.
    - `tools`: `google_search` 도구가 등록되어 있어 모델이 지식 범위를 넘어선 질문에 대해 검색을 수행할 수 있습니다.
    - `instruction`: "질문에 대한 이해한 내용을 설명하고 간결하고 명확하게 답변하세요"라는 시스템 프롬프트가 포함되어 있습니다.

## 사전 준비 사항

### 1. .env 설정
`.env` 파일은 상위 폴더(`01-basic`)에 위치해야 합니다.

```bash
GOOGLE_GENAI_USE_VERTEXAI=TRUE
GOOGLE_CLOUD_PROJECT="발급받은-프로젝트-ID"
GOOGLE_CLOUD_LOCATION="us-central1"
GOOGLE_GENAI_MODEL="gemini-2.0-flash-exp"
```

### 2. Google Cloud 인증
```bash
gcloud auth application-default login
```

## 예제 실행 방법

### adk web 인터페이스 사용
ADK는 웹 기반의 테스트 인터페이스를 제공합니다.

1. `01-basic` 폴더(최상위)에서 아래 명령어를 실행합니다:
   ```bash
   adk web
   ```
2. 브라우저에서 열린 UI의 에이전트 목록에서 `text`를 선택합니다.
3. 질문을 입력하고 에이전트가 `google_search` 도구를 호출하여 답변을 생성하는 과정을 확인합니다.
   - 예: "오늘의 서울 날씨와 주요 뉴스를 알려줘."

## 기술적 참고 사항
- **도구 호출 (Function Calling)**: 모델이 검색이 필요하다고 판단하면 자동으로 `google_search`를 호출합니다. 사용자는 이 과정을 UI의 로그 또는 실행 추적을 통해 확인할 수 있습니다.
- **프롬프트 엔지니어링**: `INSTRUCTION` 상의 답변 형식을 조정하여 에이전트의 응답 스타일을 변경할 수 있습니다.

## 라이선스
이 프로젝트는 Apache License 2.0을 따릅니다.