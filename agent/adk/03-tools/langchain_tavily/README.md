# ADK LangChain & Tavily 검색 도구 예제 (03-tools/langchain_tavily)

이 예제는 ADK의 **LangChain 연동 기능**을 사용하여 에이전트가 Tavily Search API를 웹 검색 도구로 활용하는 방법을 보여줍니다.

## 주요 개념

- **LangchainTool Wrapper**: 기존에 작성된 수많은 LangChain 도구들을 ADK 환경에서 바로 사용할 수 있도록 감싸주는 유틸리티입니다.
- **Tavily Search**: AI 에이전트 친화적인 검색 결과를 제공하는 Tavily API를 사용하여 더욱 정교한 웹 검색을 수행합니다.

## 주요 구성 요소

### 1. LangChain 도구 초기화 (`agent.py`)
- **`TavilySearchResults`**: 검색 깊이, 이미지 포함 여부, 최대 결과 수 등을 설정하여 LangChain 도구 인스턴스를 생성합니다.
- **`LangchainTool`**: `adk_tavily_tool = LangchainTool(tool=tavily_tool_instance)` 와 같이 ADK 호환 도구로 변환합니다.

### 2. 하이브리드 도구 에이전트
- **병합 활용**: 자체 정의한 Python 함수(`get_exchange_rate`)와 LangChain 기반 도구(`adk_tavily_tool`)를 동시에 에이전트에 등록하여 사용합니다.

## 사전 준비 사항
- **TAVILY_API_KEY**: [Tavily AI](https://tavily.com/)에서 발급받은 API 키를 `.env` 파일에 설정해야 합니다.

## 실행 방법
1. `.env` 파일에 `TAVILY_API_KEY`를 설정합니다.
2. `03-tools` 폴더에서 `adk web`을 실행합니다.
3. 에이전트 목록에서 `langchain_tavily`를 선택하여 다음과 같이 질문하세요:
   - "현재 달러 환율 알려줘." (Python 함수 도구 사용)
   - "최근 AI 트렌드에 대해 조사해줘." (Tavily 검색 도구 사용)

## 라이선스
이 프로젝트는 Apache License 2.0을 따릅니다.
