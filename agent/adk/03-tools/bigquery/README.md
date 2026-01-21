# Google BigQuery 도구 예제

이 폴더는 ADK 에이전트 프레임워크의 내장 BigQuery 도구를 사용하여 다양한 메타데이터를 검색하고 BigQuery 내에서 SQL 쿼리를 실행하는 방법을 보여줍니다.

## .env 설정

`.env` 파일은 상위 폴더(`03-tools`)에 위치해야 합니다. 환경 파일에 포함할 내용에 대한 자세한 내용은 다음 URL을 참조하세요:

https://google.github.io/adk-docs/get-started/quickstart/#set-up-the-model

다음은 엔터프라이즈 환경에서 Vertex AI와 함께 ADK를 사용하기 위한 예제 구성입니다:

```
GOOGLE_GENAI_USE_VERTEXAI=TRUE                  # 엔터프라이즈용 Vertex AI 사용.
GOOGLE_CLOUD_PROJECT="ai-hangsik"               # 자신의 Project ID로 변경하세요.
GOOGLE_CLOUD_LOCATION="global"                  # Global Endpoint 사용.
GOOGLE_GENAI_MODEL = "gemini-2.5-flash"         # 최신 Gemini 버전.
```

AI Studio를 사용하는 일반 사용자의 경우 다음과 같이 GOOGLE_API_KEY를 설정하세요:

```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=PASTE_YOUR_ACTUAL_API_KEY_HERE
```

## 소스 코드 실행 방법
다음 gcloud 명령어를 사용하여 Google Cloud 인증을 설정하세요:
```
gcloud auth application-default login
```

다음 명령어로 하위 에이전트 도구 예제를 실행하세요:
```
adk_workshop/adk/03-tools$ adk web
```

UI에서 bigquery를 선택하고 다음 명령을 실행하세요:

1. 메타데이터 검색
```
ai-hangsik 프로젝트에 등록된 데이터 세트를 설명해주세요.
```

2. 자연어 검색 (NL2SQL)
```
bbc_news.fulltext의 카테고리 그룹별 개수를 알려주세요. 또한 사용된 SQL 쿼리도 보여주세요.
```

## 라이선스

이 프로젝트는 Apache License 2.0을 따릅니다. 모든 코드와 콘텐츠의 저작권은 **ForusOne**(shins777@gmail.com)에 있습니다.