# ADK 루프 워크플로 에이전트 예제

이 폴더는 ADK(Agent Development Kit)를 사용한 루프 기반 워크플로 에이전트 예제를 제공합니다. 에이전트는 반복적으로 사용자 입력을 처리하며 반복적 개선, 멀티턴 질문 또는 다단계 작업이 필요한 시나리오에 적합합니다. 워크플로가 사용자와 상호 작용하거나 중지 조건이 충족될 때까지 반복 단계를 수행해야 할 때 유용합니다.

## .env 구성

ADK에 필요한 환경 변수가 포함된 `.env` 파일을 상위 디렉터리(`adk/05-workflow/`)에 생성하세요.

변수 및 인증에 대한 자세한 내용은 ADK 빠른 시작을 참조하세요:
https://google.github.io/adk-docs/get-started/quickstart/#set-up-the-model

다음 예제 변수는 엔터프라이즈 환경에서 Vertex AI와 함께 사용하는 것을 가정합니다:
```
GOOGLE_GENAI_USE_VERTEXAI=TRUE                  # 엔터프라이즈용 Vertex AI 사용.
GOOGLE_CLOUD_PROJECT="ai-hangsik"               # Project ID로 변경하세요.
GOOGLE_CLOUD_LOCATION="global"                  # 글로벌 엔드포인트 사용.
GOOGLE_GENAI_MODEL = "gemini-2.5-flash"         # 예제 Gemini 모델.
```

AI Studio를 사용하는 개인 사용자의 경우 다음과 같이 API 키를 설정하세요:
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