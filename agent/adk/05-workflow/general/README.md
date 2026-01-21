# ADK 일반 워크플로 에이전트 예제

## 1. 예제 개요
이 폴더에는 ADK(Agent Development Kit)로 구축된 일반 워크플로 에이전트 예제가 포함되어 있습니다. 이 에이전트는 사용자 입력을 처리하기 위한 구성 가능한 워크플로를 보여주며 다양한 비즈니스 시나리오에 맞게 확장하거나 사용자 지정할 수 있습니다. 이 예제는 ADK에서 다단계 또는 다중 에이전트 워크플로를 구성하는 방법을 이해하는 데 유용합니다.

## 2. 환경 설정
ADK에 필요한 환경 변수가 포함된 `.env` 파일을 상위 디렉터리(`adk/05-workflow/`)에 생성하세요.

포함할 변수에 대한 자세한 내용은 ADK 빠른 시작을 참조하세요:
https://google.github.io/adk-docs/get-started/quickstart/#set-up-the-model

다음 예제 변수는 엔터프라이즈 환경에서 Vertex AI와 함께 ADK를 사용할 때 적용됩니다:
```
GOOGLE_GENAI_USE_VERTEXAI=TRUE                  # 엔터프라이즈용 Vertex AI 사용.
GOOGLE_CLOUD_PROJECT="ai-hangsik"               # Project ID로 변경하세요.
GOOGLE_CLOUD_LOCATION="global"                  # 글로벌 엔드포인트 사용.
GOOGLE_GENAI_MODEL = "gemini-2.5-flash"         # 예제 Gemini 모델.
```

AI Studio를 사용하는 개인 사용자의 경우 아래와 같이 API 키를 설정하세요:
```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=PASTE_YOUR_ACTUAL_API_KEY_HERE
```

## 소스 코드 실행 방법
다음 명령을 사용하여 Google Cloud에 인증하세요:
```
adk_workshop/adk/05-workflow $ gcloud auth application-default login
```

ADK CLI(저장소 루트에서)를 사용하여 병렬 하위 에이전트 예제를 실행하세요:
```
adk_workshop/adk/05-workflow $ adk web
```

## 라이선스
이 프로젝트는 Apache License 2.0 라이선스를 따릅니다. 모든 코드와 콘텐츠의 저작권은 **ForusOne**(shins777@gmail.com)에 있습니다.