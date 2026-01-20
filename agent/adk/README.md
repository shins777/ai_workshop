# ADK (Agent Development Kit) 로컬 개발 환경 설정

ADK는 에이전트 구축 및 테스트를 위한 편리한 로컬 개발 환경을 제공합니다. `adk web`과 같은 명령어를 사용하면 복잡한 데이터 흐름을 쉽게 검사, 디버깅 및 이해할 수 있으므로 로컬에서 개발하는 것이 좋습니다. 로컬에서 개발이 완료되면 해당 에이전트코드를 클라우드 환경의 Runtime 에 배포해서 실행할 수 있습니다.

소스 코드는 Visual Studio Code로 개발되었지만 특정 IDE에 종속되지는 않습니다. 리포지토리를 복제하고 개발 환경에 맞는 도구를 사용하세요. 
VS Code를 설치하려면 https://code.visualstudio.com/ 을 참조하세요.

## Git 리포지토리 복제
로컬에서 리포지토리를 받으려면 다음을 실행하세요:

```
git clone https://github.com/shins777/ai_workshop.git
```

## `uv` 패키지 관리자 설치

이 프로젝트는 Python 패키지 및 프로젝트 관리자로 `uv`를 사용합니다. `uv`는 Rust로 작성된 빠르고 인체공학적인 관리자입니다.  
자세한 내용은 프로젝트를 참조하세요: https://github.com/astral-sh/uv

다음 방법 중 하나를 사용하여 `uv`를 설치할 수 있습니다:

```
curl -LsSf https://astral.sh/uv/install.sh | sh
```

또는

```
pip install uv
```

## 2. `uv`로 가상 환경 초기화

`uv`로 작업할 때 Python 가상 환경을 사용하는 것이 좋습니다.
리포지토리를 복제한 경우 `adk_workshop/adk` 아래에 `pyproject.toml` 파일이 있어야 합니다. 이 파일은 프로젝트 의존성을 정의하며 `uv`가 예제 코드를 실행하기 위한 격리된 환경을 생성할 수 있게 합니다. 개발에는 Python 3.12를 사용하는 것을 권장합니다.

가상 환경 생성:

```
cd adk_workshop/adk
uv venv --python 3.12

uv init
```

가상 환경 활성화:

```
source .venv/bin/activate
(adk) adk_workshop/adk$
```

테스트가 끝나면 환경을 비활성화하세요:

```
deactivate
```

## 3. 빠른 ADK 에이전트 테스트

간단한 ADK 에이전트 예제를 실행하여 런타임 환경을 확인합니다.

1) 환경에 ADK 패키지를 설치합니다. 2025년 7월 기준으로 이 예제는 `google-adk` 1.8.0을 대상으로 합니다:

```
(adk) adk_workshop/adk/01-agent$ uv add "google-adk[vertexai]==1.8.0"
```

2) 예제에서 사용하는 런타임 구성을 포함하는 `.env` 파일을 생성합니다. 빠른 테스트를 위해 `adk_workshop/adk/01-agent/` 안에 `.env` 파일을 만드세요.

`.env` 생성 후 예제 디렉터리 목록:

```
(adk) adk_workshop/adk/01-agent$ ls -al
total 16
-rw-r--r--   1 user  staff   198 Jun  2 08:26 .env
-rw-r--r--   1 user  staff  3178 Jun  2 08:20 README.md
drwxr-xr-x   6 user  staff   192 Jun  2 08:25 basic
drwxr-xr-x   8 user  staff   256 Jun  2 08:20 runtime
drwxr-xr-x   7 user  staff   224 Jun  2 08:26 search
```

`.env`에 필요한 변수는 ADK 퀵스타트를 참조하세요:
https://google.github.io/adk-docs/get-started/quickstart/#set-up-the-model

엔터프라이즈(Vertex AI) 예제 `.env` 변수:

```
GOOGLE_GENAI_USE_VERTEXAI=TRUE
GOOGLE_CLOUD_PROJECT="ai-hangsik"
GOOGLE_CLOUD_LOCATION="global"
GOOGLE_GENAI_MODEL="gemini-2.5-flash"
```

AI Studio / API 키 사용 시:

```
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=PASTE_YOUR_ACTUAL_API_KEY_HERE
```

3) ADK CLI를 통해 ADK 예제를 실행합니다. 필요한 경우 Google Cloud에 인증하세요:

```
gcloud auth application-default login
```

예제 UI / 런타임 시작:

```
(adk) adk_workshop/adk/01-agent$ adk web
```

채팅 인터페이스에 "생성형 AI란 무엇인가요?"와 같은 테스트 프롬프트를 입력하세요. 테스트가 올바르게 실행되면 리포지토리의 스크린샷과 유사한 ADK 웹 인터페이스가 표시되어야 합니다.

## 추가 참고 사항
- 예제는 필요한 의존성이 설치된 작동하는 Python 환경을 가정합니다. 임포트 오류가 발생하면 가상 환경과 설치된 패키지를 확인하세요.
- 리포지토리에는 빠른 실험을 위한 노트북 예제가 포함되어 있습니다. 모든 기능을 다루지는 않을 수 있습니다.
- API 키와 기타 비밀을 보호하세요. 실제 자격 증명이 포함된 `.env` 파일을 버전 제어에 커밋하지 마세요.

## 라이선스
이 프로젝트는 Apache License 2.0에 따라 라이선스가 부여됩니다. 모든 코드와 콘텐츠의 저작권은 **ForusOne** (shins777@gmail.com)에 있습니다.