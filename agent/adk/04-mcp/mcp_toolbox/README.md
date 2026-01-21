# ADK MCP Toolbox 연동 예제 (04-mcp/mcp_toolbox)

이 예제는 ADK가 **Toolbox (구 Toolbox-Core)**와 연동하여 도구를 중앙에서 관리하고 MCP로 확장하는 고급 기능을 보여줍니다.

## 주요 개념

- **Toolbox Integration**: `toolbox_core` 라이브러리를 사용하여 YAML 형식으로 정의된 도구들을 동적으로 로드합니다.
- **BigQuery 연동**: MCP를 통해 BigQuery SQL 쿼리를 실행하는 도구를 구성하는 예시를 포함합니다.

## 주요 구성 요소

### 1. 도구 정의 (`tools.yaml`)
- **소스(Sources)**: BigQuery 프로젝트 정보를 정의합니다.
- **도구(Tools)**: `query_bbc`와 같이 실제 실행될 SQL 문과 설명을 정의합니다.
- **툴셋(Toolsets)**: 관련 도구들을 묶어 관리합니다.

### 2. 에이전트 정의 (`agent.py`)
- **`get_toolbox` 함수**: `ToolboxSyncClient`를 사용하여 `tools.yaml`에 정의된 툴셋이나 개별 도구를 동적으로 로드합니다.
- **`root_agent`**: 로드된 Toolbox 도구들을 사용하여 사용자의 데이터 질의 요청을 처리합니다.

## 워크플로우 동작 방식
1. 에이전트가 시작될 때 Toolbox 클라이언트가 구성 파일을 읽습니다.
2. 사용자가 데이터 분석이나 통계 질문을 하면 `query_bbc` 도구가 활성화됩니다.
3. Toolbox는 정의된 BigQuery 소스에 쿼리를 실행하고 결과를 에이전트에 전달합니다.

## 사전 준비 사항

- **Toolbox 라이브러리**: `toolbox-core` 패키지가 설치되어 있어야 합니다.
- **BigQuery 권한**: 도구에서 사용되는 GCP 프로젝트의 BigQuery 데이터에 접근할 수 있는 인증(Credentials)이 필요합니다.

## 실행 방법

1. `tools.yaml` 내의 프로젝트명 등을 관리 중인 환경에 맞게 수정합니다.
2. `04-mcp` 폴더에서 `adk web`을 실행합니다.
3. 에이전트 목록에서 `mcp_toolbox`를 선택하여 테스트합니다.
   - 예: "BBC 뉴스 카테고리별 뉴스가 몇 개인지 알려줘."

## 기술적 참고 사항
- 이 방식은 대규모 조직에서 수많은 도구를 중앙에서 관리하고, 이를 여러 에이전트가 공유하여 사용하는 엔터프라이즈 시나리오에 적합합니다.

## 라이선스
이 프로젝트는 Apache License 2.0을 따릅니다.
