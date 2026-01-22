# a2a_agent

## 개요

`a2a_agent` 모듈은 ADK(Agent Development Kit) 프레임워크 내에서 에이전트 간(Agent-to-Agent, A2A) 통신 및 오케스트레이션을 위한 핵심 로직을 제공합니다. 서로 및 외부 서비스와 상호작용할 수 있는 에이전트의 생성, 등록 및 관리를 가능하게 합니다.

### 에이전트 구조

- **에이전트 클라이언트(Agent Client)**: 에이전트 로직의 주 진입점입니다. 에이전트 수명 주기, 메시지 처리 및 통신을 담당합니다.
- **원격 에이전트(Remote Agents)**: 도메인별 로직과 함수를 구현하는 전문 에이전트(예: 주가 정보 에이전트)입니다.
- **서브 에이전트(Sub-Agents)**: 메인 에이전트에서 호출할 수 있는 특정 작업이나 기술을 캡슐화한 모듈식 컴포넌트입니다.

- `remote_agents/stock_price/agent_stock_price` 디렉토리에는 주가 정보를 가져오고 반환할 수 있는 에이전트가 포함되어 있습니다.
- 이 에이전트는 주식 관련 쿼리를 모듈식으로 처리하기 위해 함수(`functions.py`)와 서브 에이전트(`sub_agents.py`)를 노출합니다.

## 파일 구조

```
a2a_agent/
├── agent_client/
│   └── agent.py         # 핵심 에이전트 클라이언트 로직
├── remote_agents/
│   └── stock_price/
│       └── agent_stock_price/
│           ├── agent.py       # 원격 주가 에이전트 구현
│           ├── functions.py   # 주가 조회 함수
│           └── sub_agents.py  # 서브 에이전트 정의 (회사 정보, 요약 등)
└── ...
```

## 설정

`a2a_agent` 폴더에 `.env` 파일을 생성하고 다음 설정을 입력합니다.

```
GOOGLE_GENAI_USE_VERTEXAI=TRUE
GOOGLE_CLOUD_PROJECT="발급받은-프로젝트-ID"
GOOGLE_CLOUD_LOCATION="us-central1"
GOOGLE_GENAI_MODEL = "gemini-2.0-flash"

# 주식 API 키 (https://www.alphavantage.co/ 에서 발급 가능)
STOCK_API_KEY = "발급받은-API-KEY"
```

## 실행 예시

원격 주가 에이전트를 실행하려면 다음 명령어를 사용하십시오:

```bash
adk api_server --a2a --port 8001 a2a_agent/remote_agents/stock_price
```

클라이언트를 실행하여 원격 에이전트로부터 응답을 받으려면 다음 명령어를 사용하십시오:

```bash
adk web a2a_agent/agent_client
```

다음과 같은 질문을 입력해 보세요:
```
구글의 최신 주가는 얼마인가요?
```

## 라이선스
본 프로젝트는 Apache License 2.0에 따라 라이선스가 부여됩니다. 