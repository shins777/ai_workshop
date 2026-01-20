# ADK 대화형 에이전트 - 이벤트(Event)

이 폴더는 ADK(에이전트 개발 키트) 프레임워크를 사용하여 이벤트 기반 대화형 AI 에이전트를 구축하고 운영하는 방법을 보여줍니다.  
이벤트는 ADK에서 사용자와 에이전트 간의 통신을 위한 핵심 개념입니다. 이 예제는 개별 이벤트 내부의 다양한 속성을 검사하는 방법을 보여줍니다.  
에이전트는 기본적으로 Google 검색을 사용하여 사용자 쿼리에 응답하며, 런너 스크립트는 각 단계에서 상세한 이벤트 스트리밍과 에이전트의 내부 동작을 보여줍니다. 

이 예제는 실제 이벤트에 포함된 다양한 필드를 파싱하고 검사합니다. 실제 프로젝트에서는 이벤트가 전달하는 정보를 사용하여 워크플로를 제어하거나, 작업을 트리거하거나, 결과를 표시할 수 있습니다.

## .env 구성

`.env` 파일을 상위 폴더(`02-context`)에 배치하세요. 권장되는 환경 변수 및 인증 단계는 ADK 퀵스타트를 참조하세요:
https://google.github.io/adk-docs/get-started/quickstart/#set-up-the-model

다음 환경 설정은 엔터프라이즈 환경에서 Vertex AI와 함께 ADK를 사용하기 위한 예시입니다:

```
GOOGLE_GENAI_USE_VERTEXAI = TRUE
GOOGLE_CLOUD_PROJECT = "YOUR_PROJECT_ID"
GOOGLE_CLOUD_LOCATION = "YOUR_PROJECT_LOCATION"
GOOGLE_GENAI_MODEL = "gemini-2.5-flash"
```

AI Studio를 사용하는 개인 사용자의 경우 API 키를 다음과 같이 설정하세요:

```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=PASTE_YOUR_ACTUAL_API_KEY_HERE
```

## 예제 실행

Google Cloud로 환경 인증:

```
adk_workshop/adk/02-context$ gcloud auth application-default login
```

`02-context` 폴더에서 런너 스크립트 실행:

```
adk_workshop/adk/02-context$ uv run -m event.runner
```

Runner 클래스는 코드 수준에서 이벤트를 제어하고 검사하는 프로그래밍 방식을 보여줍니다.

웹 UI를 통해 이벤트 세부 정보를 보려면 다음을 실행할 수도 있습니다:

```
adk_workshop/adk/02-context$ adk web
```

## 라이선스

이 프로젝트는 Apache License 2.0에 따라 라이선스가 부여됩니다. 