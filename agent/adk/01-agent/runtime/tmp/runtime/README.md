# ADK 런타임 에이전트 예제 - ADK 런타임 이해하기

이 폴더는 ADK(에이전트 개발 키트) 프레임워크를 사용하여 하위 에이전트 및 에이전트 도구를 활용한 고급 AI 에이전트를 구축하고 운영하는 방법을 보여줍니다.
이 예제는 Runner 클래스를 사용하는 방법을 설명합니다. 이 방식은 adk 웹 인터페이스를 통해 실행되는 것이 아니라, 실제 프로젝트의 프레젠테이션 계층에서 수행되는 것처럼 API 호출을 통해 실행됩니다. 프로덕션 환경에서는 사용자 정의 UI에서 Runner를 사용하여 에이전트를 호출하게 됩니다.

## 배경

### ADK 런타임의 이벤트 루프
아래 이미지는 ADK 런타임에서 가장 중요한 개념인 이벤트 루프를 설명합니다. 이 이벤트 루프 메커니즘은 Python의 비동기 이벤트 루프와 유사합니다.
![event loop](https://google.github.io/adk-docs/assets/event-loop.png)
이미지 출처: https://google.github.io/adk-docs/runtime/#core-idea-the-event-loop

### 호출 흐름
다음 URL을 참조하면 더 자세한 작동 프로세스를 확인할 수 있습니다.
* https://google.github.io/adk-docs/runtime/#how-it-works-a-simplified-invocation

## 개요
`runtime` 에이전트 예제는 다음을 보여줍니다:
- 긍정 및 부정 비평을 위한 하위 에이전트를 포함하는 루트 에이전트 정의
- 선택적으로 에이전트 도구로 하위 에이전트 래핑
- 환경 변수에서 구성 값 로드
- Runner 클래스를 사용하여 실행

## .env 설정

`.env` 파일은 상위 폴더(`01-agent`)에 위치해야 합니다. 환경 파일에 포함할 내용에 대한 자세한 내용은 다음 URL을 참조하세요:
https://google.github.io/adk-docs/get-started/quickstart/#set-up-the-model

다음은 엔터프라이즈 환경에서 Vertex AI와 함께 ADK를 사용하기 위한 예제 구성입니다:

```
GOOGLE_GENAI_USE_VERTEXAI = TRUE
GOOGLE_CLOUD_PROJECT = "YOUR_PROJECT_ID"
GOOGLE_CLOUD_LOCATION = "YOUR_PROJECT_LOCATION"
GOOGLE_GENAI_MODEL = "gemini-2.5-flash"
```

AI Studio를 사용하는 일반 사용자의 경우 다음과 같이 GOOGLE_API_KEY를 설정하세요:

```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=PASTE_YOUR_ACTUAL_API_KEY_HERE
```

## 파일 구조
```
adk/01-agent/runtime/
├── __init__.py
├── agent.py
├── runner.py
├── sub_agent.py
└── README.md
```

- `agent.py`: 하위 에이전트 및 에이전트 도구 통합을 포함하여 루트 에이전트의 빌드 및 설정 코드를 포함합니다.
- `runner.py`: 사용자 입력 및 에이전트 응답을 처리하기 위한 대화 루프를 실행하는 스크립트를 제공합니다.
- `sub_agent.py`: 긍정 및 부정 비평가 하위 에이전트를 정의합니다.
- `__init__.py`: 폴더를 Python 패키지로 표시합니다.


## 작동 방식

루트 에이전트는 ADK `Agent` 클래스를 사용하여 정의되며, 아래와 같이 하위 에이전트를 포함합니다.
하위 에이전트는 사용자의 질문 분석에 따라 루트 에이전트에 의해 호출되며, 쿼리에 적합한 하위 에이전트를 호출합니다.

```
    agent = Agent(
        name = "root_agent",
        model = os.getenv("MODEL"),
        description = "Agent that answers user queries",
        instruction = INSTRUCTION,
        sub_agents = [positive_critic, negative_critic],
    ) 
```

## 예제 실행
### 1. google.adk.runners.Runner 클래스를 사용하여 실행

다음 gcloud 명령어를 사용하여 Google Cloud 인증을 설정하세요:

```
gcloud auth application-default login
```

다음과 같이 `uv run` 명령어를 사용하여 runner 클래스를 실행할 수 있습니다.
```
adk_workshop/adk/01-agent$ uv run -m runtime.runner
```

또는 웹 브라우저를 통해 실행하세요:
```
ai_agent/adk/01-agent$ adk web
```


## 라이선스

이 프로젝트는 Apache License 2.0을 따릅니다. 모든 코드와 콘텐츠의 저작권은 **ForusOne** (shins777@gmail.com)에 있습니다.