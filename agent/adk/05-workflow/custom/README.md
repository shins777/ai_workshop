# 사용자 지정 워크플로 CriticAgent 예제 (ADK)

이 폴더는 ADK(Agent Development Kit)를 사용하여 사용자 지정 다단계 비평 에이전트를 구축하고 운영하는 방법을 보여줍니다. 이 예제는 긍정적, 부정적 및 종합적 검토 단계를 별도의 하위 에이전트에 위임하고 출력을 조정하여 전체 비평 워크플로를 완료하는 방법을 보여줍니다.

내용
- `agent.py`: 긍정적, 부정적 및 검토 하위 에이전트를 조정하는 루트 `CriticAgent`를 정의합니다.
- `critic.py`: 각 하위 에이전트를 순차적으로 실행하고 각 단계에 대한 이벤트를 생성하는 사용자 지정 `CriticAgent` 클래스를 구현합니다.
- `sub_agent.py`: 워크플로에서 사용하는 하위 에이전트를 정의합니다.
  - `positive_critic_agent`: 긍정적인 피드백을 생성합니다.
  - `negative_critic_agent`: 건설적인 부정적인 피드백을 생성합니다.
  - `review_critic_agent`: 비평을 집계하고 최종 검토를 생성합니다.

## .env 구성

ADK 예제에 필요한 환경 변수가 포함된 `.env` 파일을 상위 폴더(`adk/05-workflow/`)에 생성하세요.

권장 변수 및 인증 단계는 ADK 빠른 시작을 참조하세요:
https://google.github.io/adk-docs/get-started/quickstart/#set-up-the-model

Vertex AI(엔터프라이즈)용 환경 변수 예:
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

각 하위 에이전트의 작동 방식과 사용 사례에 맞게 워크플로를 조정하는 방법을 알아보려면 모듈 수준 README 파일과 소스 코드를 확인하세요.

## 라이선스
이 프로젝트는 Apache License 2.0 라이선스를 따릅니다. 모든 코드와 콘텐츠의 저작권은 **ForusOne**(shins777@gmail.com)에 있습니다.