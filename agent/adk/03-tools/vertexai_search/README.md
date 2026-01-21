# ADK Vertex AI Search 도구 예제 (03-tools/vertexai_search)

이 예제는 에이전트가 구글 클라우드의 **Vertex AI Search (Enterprise Search)** 데이터 스토어를 사용하여 방대한 비정형 데이터나 웹사이트 정보를 검색하는 방법을 보여줍니다.

## 주요 개념

- **VertexAiSearchTool**: Vertex AI Search 데이터 스토어(Data Store)와 연결되어 엔터프라이즈급 검색 기능을 에이전트 도구로 제공합니다.
- **Search-as-a-Service**: 강력한 구글 검색 엔진 기술을 기업 내부 데이터에 그대로 적용합니다.

## 주요 구성 요소

### 1. 도구 구성 (`agent.py`)
- **`data_store_id`**: 프로젝트 번호, 위치, 데이터 스토어 ID를 조합한 완전한 리소스 경로를 사용하여 데이터 스토어를 지정합니다.
- **자동 검색**: 사용자의 자연어 질문을 에이전트가 받아 내부적으로 검색 쿼리를 실행합니다.

## 사전 준비 사항
- **Vertex AI Search 데이터 스토어**: [GCP Search & Conversation](https://console.cloud.google.com/gen-app-builder)에서 데이터 스토어 및 앱을 먼저 구축해야 합니다.
- **환경 변수 설정**: 
    - `VAIS_PROJECT_NUMBER`: 구글 클라우드 프로젝트 번호
    - `VAIS_LOCATION`: 데이터 스토어 위치 (기본 "global")
    - `VAIS_DATASTORE_ID`: 생성한 데이터 스토어 ID

## 실행 방법
1. `.env` 파일에 위 3가지 환경 변수를 설정합니다.
2. `03-tools` 폴더에서 `adk web`을 실행합니다.
3. 에이전트 목록에서 `vertexai_search`를 선택하여 데이터 스토어에 업로드된 내용에 대해 질문하세요.

## 라이선스
이 프로젝트는 Apache License 2.0을 따릅니다.