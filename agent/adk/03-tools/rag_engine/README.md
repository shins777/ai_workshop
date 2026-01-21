# ADK Vertex AI RAG 엔진 도구 예제 (03-tools/rag_engine)

이 예제는 에이전트가 구글 클라우드의 **Vertex AI RAG Engine** 코퍼스를 조회하여 기업 내부 문서나 특정 도메인 정보를 바탕으로 답변하는 방법을 보여줍니다.

## 주요 개념

- **VertexAiRagRetrieval**: Vertex AI RAG Engine에 등록된 문서들(Semantic Search)을 검색하여 질문과 관련된 가장 유사한 청크(Chunks)를 가져옵니다.
- **RAG (Retrieval-Augmented Generation)**: 외부 지식을 실시간으로 검색하여 환각 현상을 줄이고 정확한 답변을 생성하는 기술입니다.

## 주요 구성 요소

### 1. RAG 도구 빌더 (`agent.py`)
- **`rag_resources`**: 환경 변수 `RAG_CORPUS`에 지정된 코퍼스 ID를 참조하여 조회 범위를 설정합니다.
- **검색 파라미터**: `similarity_top_k` (가져올 문서 개수), `vector_distance_threshold` (유사도 임계치) 등을 통해 검색 품질을 조절합니다.

### 2. 에이전트 지침
- **Instruction**: 사용자의 의도를 먼저 파악하고, 참조된 문서를 명시하며, 최종 답변을 요약하도록 답변 구조를 강제합니다.

## 사전 준비 사항
- **GCP RAG Engine 설정**: Vertex AI Console에서 RAG 코퍼스를 생성하고 문서를 업로드해야 합니다.
- **환경 변수**: 생성된 코퍼스의 리소스 ID를 `.env` 파일의 `RAG_CORPUS` 항목에 설정하세요.

## 실행 방법
1. `.env` 파일에 `RAG_CORPUS` 정보가 올바른지 확인합니다.
2. `03-tools` 폴더에서 `adk web`을 실행합니다.
3. 에이전트 목록에서 `rag_engine`을 선택하여 등록된 문서에 관한 질문을 던집니다.

## 라이선스
이 프로젝트는 Apache License 2.0을 따릅니다.
