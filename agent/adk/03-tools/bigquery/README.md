# ADK BigQuery 도구 예제 (03-tools/bigquery)

이 예제는 에이전트가 구글 클라우드의 **BigQuery** 데이터베이스와 직접 상호작용하여 데이터를 쿼리하고 분석하는 방법을 보여줍니다.

## 주요 개념

- **BigQueryToolset**: BigQuery 데이터 탐색, SQL 생성 및 실행을 위한 도구 모음입니다.
- **Write Mode Control**: 에이전트가 데이터를 수정하거나 삭제하는 것을 방지하기 위해 쓰기 모드를 제한할 수 있습니다.

## 주요 구성 요소

### 1. 도구 세트 구성 (`agent.py`)
- **`BigQueryToolConfig`**: `write_mode=WriteMode.BLOCKED` 설정을 통해 안전하게 조회용으로만 도구를 구성합니다.
- **인증 설정**: `google.auth.default()`를 사용하여 애플리케이션 기본 자격 증명(ADC)을 자동으로 로드합니다.
- **`BigQueryToolset`**: 데이터 세트 목록 조회, 테이블 스키마 확인, SQL 실행 등의 기능을 에이전트에게 부여합니다.

### 2. 에이전트 정의
- **`root_agent`**: BigQuery 도구 세트를 사용하여 자연어 질문을 SQL로 변환하고 결과를 분석하여 답변합니다.

## 사전 준비 사항
- **GCP 인증**: 터미널에서 `gcloud auth application-default login`을 실행하여 로컬 환경에 인증 정보를 설정하세요.
- **권한**: 사용 중인 GCP 프로젝트의 BigQuery 데이터에 대해 `BigQuery Data Viewer` 및 `BigQuery Job User` 권한이 필요합니다.

## 실행 방법
1. `.env` 파일에 관련 GCP 프로젝트 설정이 되어 있는지 확인합니다.
2. `03-tools` 폴더에서 `adk web`을 실행합니다.
3. 에이전트 목록에서 `bigquery`를 선택하여 다음과 같이 질문하세요:
   - "내 프로젝트에 있는 데이터 세트 목록을 알려줘."
   - "특정 테이블의 상위 5개 행을 보여줘."

## 라이선스
이 프로젝트는 Apache License 2.0을 따릅니다.