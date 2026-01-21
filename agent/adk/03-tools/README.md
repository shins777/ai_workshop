# ADK 도구(Tools) 통합 가이드 (03-tools)

이 디렉토리는 ADK(Agent Development Kit) 에이전트의 능력을 확장하는 다양한 **도구(Tools)** 활용 예제를 제공합니다. 에이전트는 도구를 통해 실시간 웹 검색, 데이터베이스 쿼리, 코드 실행 및 외부 API 연동 등 모델의 지식 범위를 넘어선 작업을 수행할 수 있습니다.

## 포함된 도구 예제 목록

### 1. [FUNCTION_CALL (Python 함수 호출)](./function_call/README.md)
- **핵심**: 일반 Python 함수를 도구로 변환.
- **예시**: 실시간 환율 조회, 주가 정보 검색 API 연동.

### 2. [GOOGLE_SEARCH (구글 검색)](./google_search/README.md)
- **핵심**: ADK 내장 웹 검색 도구 활용.
- **예시**: 인터넷상의 최신 뉴스와 정보를 실시간으로 검색하여 답변.

### 3. [CODE_EXECUTION (Python 코드 실행)](./code_execution/README.md)
- **핵심**: 에이전트가 코드를 작성하고 직접 실행.
- **예시**: 정확한 수학 연산 및 복잡한 데이터 처리.

### 4. [BIGQUERY (구글 클라우드 데이터 분석)](./bigquery/README.md)
- **핵심**: 데이터웨어하우스 BigQuery 연동.
- **예시**: 자연어로 데이터베이스 질의 및 통계 분석 결과 도출.

### 5. [AGENT_TOOL (에이전트를 도구로 사용)](./agent_tool/README.md)
- **핵심**: 하위 에이전트를 도구로 래핑.
- **예시**: 전문 비평가 에이전트에게 특정 업무를 위임하는 계층적 구조.

### 6. [LANGCHAIN_TAVILY (LangChain 에코시스템 활용)](./langchain_tavily/README.md)
- **핵심**: LangChain 도구 라이브러리 연동.
- **예시**: Tavily Search API 등 LangChain의 방대한 도구 자원 활용.

### 7. [RAG_ENGINE (Vertex AI RAG 통합)](./rag_engine/README.md)
- **핵심**: 기업 내부 문서 기반의 지식 검색.
- **예시**: RAG 엔진 코퍼스 조회를 통한 정확한 근거 기반 답변.

### 8. [VERTEXAI_SEARCH (엔터프라이즈 검색)](./vertexai_search/README.md)
- **핵심**: Vertex AI Search 데이터 스토어 연동.
- **예시**: 대규모 비정형 데이터 및 웹 저장소에 대한 고도화된 검색 서비스.

---

## 공통 실행 및 테스트 방법

ADK는 모든 도구 예제를 하나의 웹 인터페이스에서 통합 테스트할 수 있는 기능을 제공합니다.

1. `03-tools` 폴더 또는 하위 폴더에서 명령어를 실행합니다:
   ```bash
   adk web
   ```
2. 웹 UI가 열리면, 왼쪽 에이전트 목록에서 테스트하고 싶은 도구(예: `google_search`, `bigquery` 등)를 선택합니다.
3. 질문을 던지고, 에이전트가 어떤 도구를 호출하여 답변을 생성하는지 실시간 로그를 통해 확인하세요.

## 라이선스
이 프로젝트는 Apache License 2.0을 따릅니다.