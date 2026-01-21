# Toolbox 에이전트 예제 (ADK)

이 폴더는 ADK(Agent Development Kit) 환경에서 ToolboxSyncClient를 사용하여 BigQuery와 같은 외부 데이터 소스와 연결하는 Toolbox 에이전트의 예제를 제공합니다.

이 예제를 실행하기 전에 데이터베이스용 MCP Toolbox를 이해하고 설치해야 합니다.

* 데이터베이스용 MCP Toolbox
    * https://googleapis.github.io/genai-toolbox/getting-started/introduction/

* MCP Toolbox 설치
    * 설치 지침은 MCP Toolbox GitHub를 참조하세요:
    * https://github.com/googleapis/genai-toolbox

    ```
    # MacOS 사용자용
    brew install mcp-toolbox
    ```

## .env 구성

`.env` 파일은 상위 폴더(`04-mcp`)에 위치해야 합니다. 환경 파일에 포함할 내용에 대한 자세한 내용은 다음 URL을 참조하세요:
https://google.github.io/adk-docs/get-started/quickstart/#set-up-the-model

다음 환경 설정은 엔터프라이즈 환경에서 Vertex AI와 함께 ADK를 사용하기 위한 예제입니다:

```
GOOGLE_GENAI_USE_VERTEXAI=TRUE                  # 엔터프라이즈용 Vertex AI 사용.
GOOGLE_CLOUD_PROJECT="ai-hangsik"               # 자신의 Project ID로 변경하세요.
GOOGLE_CLOUD_LOCATION="global"                  # 글로벌 엔드포인트 사용.
GOOGLE_GENAI_MODEL = "gemini-2.5-flash"         # 최신 Gemini 모델.

# Toolbox 구성
TOOLBOX_SYNC_CLIENT = "http://127.0.0.1:5000"

```

`AI Studio`를 사용하는 일반 사용자의 경우 다음과 같이 GOOGLE_API_KEY를 설정하세요:
```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=PASTE_YOUR_ACTUAL_API_KEY_HERE

```

## tools.yaml 예제

toolbox에서 도구를 설정하려면 아래와 같이 yaml 파일을 생성하세요. 파일 이름은 일반적으로 `tools.yaml`입니다.
BigQuery 구성에 대한 자세한 내용은 다음 URL을 참조하세요:
* https://googleapis.github.io/genai-toolbox/samples/bigquery/mcp_quickstart/


```yaml
sources:
  bigquery-bbc:
    kind: "bigquery"
    project: "ai-hangsik"

tools:
  query_bbc:
    kind: "bigquery-sql"
    source: "bigquery-bbc"
    statement:
      SELECT category, count(*) 
      FROM `ai-hangsik.bbc_news.fulltext` 
      group by category
    description: "Query the number of BBC news articles by category."

toolsets:
  my_bq_toolset:
    - query_bbc
```

## 예제 실행

다음 gcloud 명령어를 사용하여 Google Cloud 인증을 설정하세요:
```
gcloud auth application-default login
```

### MCP Toolbox 실행
새 콘솔 창을 열고 다음과 같이 toolbox를 시작하세요:
```
toolbox --tools-file "tools.yaml"
```

### 에이전트 실행
마찬가지로 셸에서 GCP 인증이 필요합니다:
```
gcloud auth application-default login
```
다음 명령어로 Toolbox 에이전트 예제를 실행하세요:
```
adk_workshop/adk/04-mcp $ adk web
```
toolbox 에이전트를 선택한 후 "Show me the BBC table."이라고 질문해 보세요.

## 라이선스

이 프로젝트는 Apache License 2.0을 따릅니다. 모든 코드와 콘텐츠의 저작권은 **ForusOne**(shins777@gmail.com)에 있습니다.
