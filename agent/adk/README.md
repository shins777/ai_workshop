# ADK (Agent Development Kit) 종합 가이드

ADK(Agent Development Kit)는 Google Cloud Platform(GCP)과 Vertex AI를 기반으로 엔터프라이즈급 AI 에이전트를 쉽고 빠르게 구축, 테스트 및 배포할 수 있도록 설계된 프레임워크입니다. 

이 리포지토리는 ADK의 핵심 기능부터 고급 워크플로우 패턴, 외부 도구 연동(MCP), A2A 등 실무에 필요한 모든 예제를 담고 있습니다.

---

## 🚀 시작하기

ADK는 `adk web` 명령어를 통해 로컬 웹 인터페이스에서 에이전트의 동작을 실시간으로 확인하고 디버깅할 수 있는 강력한 개발 환경을 제공합니다.

### 1. 가상 환경 설정

이 프로젝트는 `uv` 패키지 관리자를 사용하여 빠르고 격리된 환경을 구축합니다.
uv는 Rust로 작성된 빠르고 사용하기 쉬운 관리자입니다. 자세한 내용은 다음 프로젝트를 참조하세요. https://github.com/astral-sh/uv
uv는 다음 방법 중 하나로 설치할 수 있습니다.
```bash
# curl 로 설치
curl -LsSf https://astral.sh/uv/install.sh | sh

# pip 로 설치
pip install uv
```

테스트 환경 구성을 위한 가상환경 설정은 아래와 같습니다.
```bash
# 디렉토리 이동
cd agent/adk

# 가상 환경 생성 및 활성화
uv venv --python 3.12
source .venv/bin/activate

# activate 처리 결과
(adk) /Users/ai_user/Documents/Antigravity/ai_workshop/agent/adk$ 

# 패키지 의존성 설치, 패키지 의존성은 pyproject.toml 참고.
uv sync
```

```bash
# 모든 테스트가 끝나고 deactive 할 때는 폴더 위치 상관없이 실행
deactivate

# deactivate 실행결과
/Users/ai_user/Documents/Antigravity/ai_workshop/agent/adk$ 
```

### 2. 환경 변수 설정 (.env)
루트 폴더(ai_workshop/agent/adk) 하위에 `.env` 파일을 생성하고 필요한 자격 증명을 설정하세요.
```env

####################################################
#    Environment Variables
####################################################

# 01-basic/text
GOOGLE_GENAI_USE_VERTEXAI=TRUE
GOOGLE_CLOUD_PROJECT="ai-project"
GOOGLE_CLOUD_LOCATION="us-central1"
GOOGLE_GENAI_MODEL="gemini-2.5-flash"
# 01-basic/live
GOOGLE_GENAI_LIVE_MODEL = "gemini-live-2.5-flash"
# 01-basic/engine
AGENT_ENGINE_BUCKET = "gs://agent_engine_0120"

# 03-tools/function_call
STOCK_API_KEY = "AAAAAAAAAAAAAA"
# 03-tools/Taviliy API keys
TAVILY_API_KEY = "AAAAAAAAAAAAAA"
# 03-tools/RAG Engine
RAG_CORPUS="projects/ai-project/locations/us-central1/ragCorpora/00000000000000000"
# 03-tools/Vertex AI Search 
VAIS_PROJECT_NUMBER = "000000000000"
VAIS_LOCATION = "global"
VAIS_DATASTORE_ID = "AAAAAAAAAAAAAA"

# 04-mcp/ Toolbox configuration
TOOLBOX_SYNC_CLIENT = "http://127.0.0.1:5000"
# 04-mcp/ Google Map API key
GOOGLE_MAPS_API_KEY = "AAAAAAAAAAAAAA"

# 08-misc/model
OLLAMA_API_BASE="http://localhost:11434"
# 08-misc/agentops
AGENTOPS_API_KEY = "AAAAAAAAAAAAAA"
```

### 3. 에이전트 실행 및 테스트
`adk web` 명령어를 실행하면 모든 예제를 하나의 UI에서 통합 테스트할 수 있습니다.
```bash
adk web
```

### 4. ipynb 환경에 위에서 설정한 파이썬 가상환경으로 커널 선택하는 법

1. VS Code에서 Ctrl + Shift + P (Mac: Cmd + Shift + P)를 누릅니다.  
2. 입력창에 **Python: Select Interpreter**를 입력하고 선택합니다.  
3. 목록에서 사용하고자 하는 파이썬 버전이나 가상환경 경로를 선택합니다.

만일 가상환경이 보이지 않으면, 아래와 같이 등록합니다.

1. VS Code Setting 창으로 갑니다.  
2. 검색 박스에 "Default Interpreter Path" 를 검색하면  
   Python: Default Interpreter Path 가 보이고 해당 란에 아래와 유사하게 가상환경의 python 파일 위치를 지정합니다.   
   ```
   /Users/ai_user/Documents/Antigravity/ai_workshop/agent/adk/.venv/bin/python 
   ```
3. 위와 같이 가상환경을 설정하면 VS CODE 내의 ipynb 에서 커널 선택할때 위에서 설정한 파이썬 경로를 선택할수 있습니다.   


---

## 📁 디렉토리 구조 및 핵심 기능 가이드

ADK의 기능은 학습 단계와 주제별로 구분되어 있습니다.

### [01-basic: 기초 에이전트 구축](./01-basic/README.md)
에이전트의 가장 기본적인 구성 요소와 실행 방식을 다룹니다.
- **Engine**: Vertex AI Agent Engine 배포 및 실행 기반.
- **Runner**: 멀티 에이전트 시스템 가동 및 메시지 라우팅.
- **Live/Text**: 실시간 멀티모달(Gemini Live) 및 텍스트 기반 검색 에이전트.

### [02-context: 문맥 및 기억 관리](./02-context/README.md)
에이전트가 대화의 흐름을 기억하고 상태를 유지하는 기법을 소개합니다.
- **Session**: 대화 이력 저장 및 세션별 상태 격리.
- **Memory Bank**: 벡터 데이터베이스를 활용한 장기 기억과 정보 회상.
- **State/Event**: 복잡한 비즈니스 로직을 위한 상태 제어 및 이벤트 처리.

### [03-tools: 도구(Tools) 통합](./03-tools/README.md)
에이전트에게 강력한 권한(웹 검색, 데이터 분석, 계산 등)을 부여하는 다양한 도구 연동 예제입니다.
- **Google Search**: 실시간 웹 검색 도구.
- **BigQuery**: 엔터프라이즈 데이터웨어하우스 질의 및 분석.
- **Code Execution**: 정확한 연산을 위한 Python 코드 실행기.
- **Agent Tool**: 하위 에이전트를 도구로 호출하는 계층형 아키텍처.
- **External Search**: Tavily(LangChain), Vertex AI Search, RAG Engine 연동.

### [04-mcp: Model Context Protocol](./04-mcp/README.md)
표준화된 프로토콜인 MCP를 통해 로컬 파일 시스템, 외부 API, 원격 서버와 상호작용합니다.
- **Filesystem/Google Map**: 표준 MCP 서버 활용 예제.
- **Local/Remote Server**: 커스텀 MCP 서버 구축 및 Cloud Run 배포.

### [05-workflow: 고급 워크플로우 패턴](./05-workflow/README.md)
단일 에이전트를 넘어 복잡한 협업 구조를 설계하는 방법입니다.
- **Sequential/Parallel**: 순차적 파이프라인 및 병렬 처리.
- **Loop**: 답변 결과가 만족스러울 때까지 반복하는 자기 개선 루프.
- **Orchestration**: 중앙 에이전트가 하위 전문가들에게 업무를 할당하는 구조.

### [06-callback: 실행 제어 및 가드레일](./06-callback/README.md)
에이전트의 실행 수명 주기(Life Cycle)에 개입하여 제어 로직을 삽입합니다.
- **Agent/Model/Tool Hooks**: 호출 전후에 인자 보정, 결과 가공, 부적절한 요청/응답 차단(Guardrail) 구현.

### [07-misc: 기타 고급 확장 기능](./07-misc/README.md)
관측성, 다중 모델 연동 등 실 서비스 도입 시 필수적인 기능을 다룹니다.
- **AgentOps**: 에이전트 성능 모니터링 및 트레이싱.
- **LiteLLM**: OpenAI, Claude 등 타사 LLM 제공자 통합.
- **Ollama**: 보안 강화를 위한 로컬 환경(Llama, Gemma) 에이전트 구동.
- **Structured Output**: Pydantic 스키마 기반의 JSON 규격 보장.

---

## 🛠️ 권장 기술 스택
- **Language**: Python 3.12+
- **Framework**: `google-adk`
- **Infrastructure**: Vertex AI / Google Cloud
- **Dev Tools**: `uv`, GCP Cloud SDK, Visual Studio Code

## 📜 라이선스
이 프로젝트는 **Apache License 2.0**을 따릅니다. 모든 코드와 콘텐츠의 저작권은 **ForusOne**(shins777@gmail.com)에 있습니다.