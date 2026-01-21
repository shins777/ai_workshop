# 서브 에이전트 도구 예제 (ADK)
ADK에서는 서브 에이전트를 도구(Tool)로 사용할 수 있습니다. 에이전트를 도구로 사용하는 것과 서브 에이전트로 사용하는 것에는 중요한 차이가 있습니다.
 * 에이전트를 도구로 사용: 호출하는 에이전트가 다른 도구를 사용할 때와 마찬가지로 모든 출력에 대한 제어 권한을 가집니다.
   * 이 경우 등록된 모든 도구를 호출할 수 있습니다.
 * 에이전트를 서브 에이전트로 사용: 호출하는 에이전트가 호출된 서브 에이전트에 출력 제어 권한을 위임합니다.
   * 이 경우 특정 서브 에이전트 하나만 호출됩니다.

## 예제 개요
이 폴더는 ADK 에이전트 내에서 서브 에이전트를 도구로 활용하여 모듈식이고 구성 가능한 워크플로를 구현하는 방법을 보여줍니다.

## .env 설정

`.env` 파일은 상위 폴더(`03-tools`)에 위치해야 합니다. 환경 파일에 포함할 내용에 대한 자세한 내용은 다음 URL을 참조하세요:

https://google.github.io/adk-docs/get-started/quickstart/#set-up-the-model

다음은 엔터프라이즈 환경에서 Vertex AI와 함께 ADK를 사용하기 위한 예제 구성입니다:

```
GOOGLE_GENAI_USE_VERTEXAI=TRUE                  # 기업용 Vertex AI 사용.
GOOGLE_CLOUD_PROJECT="ai-hangsik"               # 각자 Project ID 로 변경.
GOOGLE_CLOUD_LOCATION="global"                  # Global Endpoint 사용.
GOOGLE_GENAI_MODEL = "gemini-2.5-flash"         # 현재 Gemini 최신 버전.
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

다음 명령어로 서브 에이전트 도구 예제를 실행하세요:
```
adk_workshop/adk/03-tools$ adk web
```

## 라이선스

이 프로젝트는 Apache License 2.0을 따릅니다. 모든 코드와 콘텐츠의 저작권은 **ForusOne** (shins777@gmail.com)에 있습니다.