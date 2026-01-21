# Vertex AI Search 도구 예제 (ADK)

이 폴더는 ADK 에이전트와 내장된 Vertex AI Search 도구를 사용하여 Vertex AI Search 데이터 스토어를 기반으로 사용자 쿼리에 답변하는 방법을 보여줍니다.

## .env 설정

`.env` 파일은 상위 폴더(`03-tools`)에 위치해야 합니다. 환경 파일에 포함할 내용에 대한 자세한 내용은 다음 URL을 참조하세요:
https://google.github.io/adk-docs/get-started/quickstart/#set-up-the-model

다음 환경 설정은 엔터프라이즈 환경에서 Vertex AI와 함께 ADK를 사용하기 위한 예제입니다:
```
GOOGLE_GENAI_USE_VERTEXAI=TRUE                  # 엔터프라이즈용 Vertex AI 사용.
GOOGLE_CLOUD_PROJECT="ai-hangsik"               # 자신의 Project ID로 변경하세요.
GOOGLE_CLOUD_LOCATION="global"                  # 글로벌 엔드포인트 사용.
GOOGLE_GENAI_MODEL = "gemini-2.5-flash"         # 최신 Gemini 모델.

# Vertex AI Search 구성
VAIS_PROJECT_NUMBER = "700000000000"
VAIS_LOCATION = "global"
VAIS_DATASTORE_ID = "alphabet-contracts-id2"
```

`AI Studio`를 사용하는 일반 사용자의 경우 다음과 같이 GOOGLE_API_KEY를 설정하세요:
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

UI에서 vertexai_search를 선택하고 Vertex AI Search에 등록된 정보를 조회하세요.
```
구글의 2024년 매출 현황을 알려주세요.
```

## 라이선스

이 프로젝트는 Apache License 2.0을 따릅니다. 모든 코드와 콘텐츠의 저작권은 **ForusOne**(shins777@gmail.com)에 있습니다.