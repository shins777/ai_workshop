# ADK 01-Agent 예제

이 디렉터리는 ADK(에이전트 개발 키트)를 사용한 에이전트 구현 예제를 포함하고 있습니다. 각 하위 폴더는 기본 설정부터 고급 런타임 및 검색 지원 에이전트까지 다양한 접근 방식을 보여줍니다.

## ADK 구성 요소
아래 이미지는 ADK 프레임워크의 주요 구성 요소를 보여줍니다:
![adk component](https://github.com/ForusOne/adk_agent/blob/main/images/adk_components.png?raw=true)

## 에이전트 계층 구조 (Hierarchy)
ADK를 사용하면 **단일 프로세스 내**에서 멀티 에이전트 시스템을 구축할 수 있습니다. 여러 하위 에이전트와 도구를 결합하여 멀티 에이전트 시스템을 만들 수 있지만, 모든 처리는 하나의 프로세스 내에서 모놀리식으로 처리됩니다.
![Agent Hierarchy](https://github.com/ForusOne/adk_agent/blob/main/images/multi-agent.png?raw=true)


## 01-agent 로직 및 구조

`01-agent` 예제는 ADK 기반 에이전트 시스템의 기본 로직과 구조를 보여줍니다:

- **에이전트 초기화**: ADK를 사용하여 루트 에이전트와 여러 하위 에이전트를 정의하고 초기화합니다.
- **메시지 라우팅**: 사용자 입력은 루트 에이전트가 받으며, 루트 에이전트는 처리를 위해 적절한 하위 에이전트나 도구로 메시지를 라우팅합니다.
- **역할 할당**: 각 하위 에이전트는 특정 작업(예: 비평, 정보 검색)을 담당하며, 루트 에이전트는 이들의 출력을 결합하여 최종 응답을 생성합니다.
- **모놀리식 실행**: 모든 에이전트와 도구가 단일 프로세스 내에서 실행되므로 관리와 배포가 간단합니다.

## .env 구성

환경 변수 설정에 대해서는 다음 URL을 참조하세요:
https://google.github.io/adk-docs/get-started/quickstart/#set-up-the-model 

다음은 Vertex AI를 사용하는 엔터프라이즈 환경을 위한 예제 구성입니다:

```
GOOGLE_GENAI_USE_VERTEXAI=TRUE
GOOGLE_CLOUD_PROJECT="YOUR_PROJECT_ID"
GOOGLE_CLOUD_LOCATION="YOUR_PROJECT_LOCATION"
GOOGLE_GENAI_MODEL="gemini-2.5-flash"
```

AI Studio를 사용하는 일반 사용자의 경우 다음과 같이 `GOOGLE_API_KEY`를 설정하세요:

```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=PASTE_YOUR_ACTUAL_API_KEY_HERE
```

## 시작하기

1. 실행할 예제에 따라 하위 폴더 중 하나를 선택하세요.
2. 구체적인 설정 및 사용 지침은 선택한 하위 폴더의 README 파일을 검토하세요.
3. 선택한 예제에 따라 상위 폴더에 `.env` 파일을 배치하세요.
4. 선택한 예제에 설명하는 명령어를 사용하여 에이전트를 실행하세요.

## 라이선스

이 프로젝트는 Apache License 2.0에 따라 라이선스가 부여됩니다. 