# a2a_tool

## 개요

`a2a_tool` 모듈은 ADK(Agent Development Kit) 프레임워크 내에서 에이전트 간(Agent-to-Agent, A2A) 상호작용을 구축하고 확장하기 위한 도구와 유틸리티를 제공합니다. 이 모듈에는 A2A 에이전트 시스템에 통합할 수 있는 재사용 가능한 컴포넌트, 원격 에이전트 템플릿 및 함수 모듈이 포함되어 있습니다.

### 도구 구조

- **원격 에이전트(Remote Agents)**: 환율 정보 에이전트와 같이 독립적인 서비스로 실행되어 다른 에이전트와 통신할 수 있는 원격 에이전트의 템플릿과 구현체를 포함합니다.
- **함수(Functions)**: 에이전트나 서브 에이전트에서 호출할 수 있는 모듈화된 함수(예: 환율 정보 조회 등)를 제공합니다.
- **서브 에이전트(Sub-Agents)**: 특정 기술이나 작업을 캡슐화하는 서브 에이전트를 정의하여 유연하고 확장 가능한 에이전트 설계를 가능하게 합니다.

- `remote_agents/exchange_rate/agent_exchange_rate` 디렉토리에는 환율 정보를 가져오고 반환할 수 있는 원격 에이전트가 포함되어 있습니다.
- 서브 에이전트들은 `sub_agent.py`에 구현되어 시장 정보 조회, 요약 등의 작업을 모듈식으로 처리합니다.

## 파일 구조

```
a2a_tool/
├── agent_client/
│   ├── agent.py       # 메인 오케스트레이터 에이전트
│   └── sub_agent.py   # 서브 에이전트 정의 (시장 정보, 요약 등)
├── remote_agents/
│   └── exchange_rate/
│       └── agent_exchange_rate/
│           └── agent.py   # 원격 환율 에이전트 구현
└── ...
```

## 설정

`a2a_tool` 폴더에 `.env` 파일을 생성하고 다음 설정을 입력합니다.

```
GOOGLE_GENAI_USE_VERTEXAI=TRUE
GOOGLE_CLOUD_PROJECT="발급받은-프로젝트-ID"
GOOGLE_CLOUD_LOCATION="us-central1"
GOOGLE_GENAI_MODEL = "gemini-2.0-flash"
```

## 실행 예시

원격 에이전트를 실행하려면 다음 명령어를 사용하십시오:

```bash
adk api_server --a2a --port 8001 a2a_tool/remote_agents/exchange_rate
```

클라이언트를 실행하여 원격 에이전트와 상호작용하려면 다음 명령어를 사용하십시오:

```bash
adk web a2a_tool/agent_client
```

에이전트에게 물어볼 수 있는 질문 예시:

```
현재 원/달러 환율은 얼마인가요?
```

## 라이선스
본 프로젝트는 Apache License 2.0에 따라 라이선스가 부여됩니다.