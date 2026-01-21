# ADK 로컬 모델 예제 - Ollama 연동 (07-misc/ollama_agent)

이 예제는 ADK(Agent Development Kit)에서 **Ollama**를 사용하여 로컬 환경에 설치된 LLM(예: Llama 3, Gemma)을 에이전트의 두뇌로 활용하는 방법을 보여줍니다.

## 주요 개념

- **Ollama**: 로컬 PC에서 대규모 언어 모델을 쉽게 실행하고 관리할 수 있게 해주는 오픈소스 프로젝트입니다.
- **Local-first Agent**: 외부 클라우드 API 호출 없이 로컬 자원만으로 에이전트를 구동하여 뛰어난 보안성과 데이터 프라이버시를 보장합니다.

## 주요 구성 요소

### 1. 에이전트 빌더 (`agent.py`)
- **`LiteLlm(model="ollama/...")`**: ADK의 LiteLLM 통합 기능을 통해 로컬 Ollama 엔드포인트와 통신합니다. (`llama3.2`, `gemma3` 등 지원)
- **`build_agent`**: 지정된 모델 이름을 기반으로 로컬 에이전트 인스턴스를 생성하는 함수입니다.

### 2. 단위 테스트 (`ollama_unittest.py`)
- 에이전트가 로컬 모델과 정상적으로 통신하는지 확인하기 위한 간단한 스크립트입니다.

## 사전 준비 사항

1. [Ollama 공식 홈페이지](https://ollama.com/)에서 설치 파일을 다운로드하고 설치하세요.
2. 원하는 모델을 다운로드합니다:
   ```bash
   ollama pull llama3.2
   ollama pull gemma3
   ```
3. `.env` 파일에 Ollama API 주소를 설정합니다 (기본값: `http://localhost:11434`):
   ```env
   OLLAMA_API_BASE=http://localhost:11434
   ```

## 실행 및 테스트 방법

1. Ollama 서비스가 실행 중인지 확인합니다 (`ollama list` 명령어로 확인).
2. `07-misc` 폴더에서 `adk web`을 실행합니다.
3. `ollama_agent`를 선택하고 질문을 던집니다.
4. (선택 사항) 터미널에서 `python ollama_unittest.py`를 실행하여 직접 통신을 확인합니다.

## 특징
- **비용 절감**: API 호출당 비용이 발생하지 않습니다.
- **오프라인 동작**: 인터넷 연결이 없어도 기본적인 에이전트 기능을 사용할 수 있습니다.

## 라이선스
이 프로젝트는 Apache License 2.0을 따릅니다.
