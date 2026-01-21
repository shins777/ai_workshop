# ADK Observability 예제 - AgentOps 통합 (07-misc/agentops)

이 예제는 ADK(Agent Development Kit)로 구축된 AI 에이전트의 실행 과정을 모니터링하고 분석하기 위해 **AgentOps**를 통합하는 방법을 보여줍니다.

## 주요 개념

- **Observability (관측성)**: 에이전트의 내부 동작(LLM 호출, 도구 실행, 지연 시간 등)을 실시간으로 추적하여 성능을 최적화하고 문제를 디버깅합니다.
- **AgentOps**: 에이전트 개발자를 위한 특화된 모니터링 플랫폼으로, 세션 추적, 비용 분석, 성공률 측정 등의 기능을 제공합니다.

## 주요 구성 요소

### 1. 에이전트 정의 (`agent.py`)
- **`agentops.init`**: 에이전트 실행 전에 AgentOps SDK를 초기화하고 API 키를 설정합니다. `adk-app-trace`와 같은 추적 이름을 지정할 수 있습니다.
- **자동 추적**: `agentops.init`이 호출되면 ADK 내부에서 발생하는 LLM 상호작용이 AgentOps 대시보드로 자동 전송됩니다.

## 사전 준비 사항

1. [AgentOps](https://app.agentops.ai/)에 가입하고 프로젝트 API 키를 발급받으세요.
2. `.env` 파일에 다음과 같이 키를 설정합니다:
   ```env
   AGENTOPS_API_KEY="your-agentops-api-key"
   ```

## 실행 및 테스트 방법

1. `07-misc` 폴더 내에 `.env` 파일이 있는지 확인합니다.
2. `07-misc` 폴더에서 명령어를 실행합니다:
   ```bash
   adk web
   ```
3. 웹 UI에서 `agentops` 에이전트를 선택하고 질문을 던집니다.
4. [AgentOps 대시보드](https://app.agentops.ai/)에 접속하여 실시간으로 생성되는 트레이스(Trace)와 세션 정보를 확인하세요.

## 특징
- **에이전트 수명 주기 추적**: 세션 시작부터 종료까지의 모든 이벤트를 한 화면에서 볼 수 있습니다.
- **LLM 성능 분석**: 토큰 사용량, 응답 시간, 모델별 성능 지표를 제공합니다.

## 라이선스
이 프로젝트는 Apache License 2.0을 따릅니다.