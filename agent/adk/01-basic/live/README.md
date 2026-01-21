# ADK Gemini Live 에이전트 예제 (01-basic/live)

이 폴더는 ADK(에이전트 개발 키트)를 사용하여 **Gemini Multimodal Live API**를 기반으로 한 실시간 상호작용 에이전트를 구축하는 방법을 보여줍니다. Gemini Live는 텍스트뿐만 아니라 오디오 및 비디오를 통한 실시간 고성능 상호작용을 지원합니다.

## 주요 특징

- **실시간 상호작용**: 낮은 지연 시간(Low Latency)으로 사용자와 대화가 가능합니다.
- **멀티모달 지원**: 오디오 및 비디오 데이터를 실시간으로 처리할 수 있습니다.
- **간결한 응답**: 실시간 대화의 특성상 에이전트가 짧고 명확하게 답변하도록 설계되었습니다.

## 구성 파일 설명

- **`agent.py`**: Gemini Live 모델을 사용하는 에이전트를 정의합니다.
    - `model`: `GOOGLE_GENAI_LIVE_MODEL` 환경 변수를 통해 지정된 모델을 사용합니다 (예: `gemini-2.0-flash-exp`).
    - `instruction`: 실시간 대화에 적합하도록 "가능하면 짧은 문장으로 답변해야 합니다"라는 지침이 포함되어 있습니다.

## 사전 준비 사항

### 1. .env 설정
`.env` 파일은 상위 폴더(`01-basic`)에 위치해야 합니다.

```bash
GOOGLE_GENAI_USE_VERTEXAI=TRUE
GOOGLE_CLOUD_PROJECT="발급받은-프로젝트-ID"
GOOGLE_CLOUD_LOCATION="us-central1" # Gemini Live는 현재 us-central1에서 가장 안정적입니다.
GOOGLE_GENAI_MODEL="gemini-2.0-flash-exp"
GOOGLE_GENAI_LIVE_MODEL="gemini-2.0-flash-exp" # Live API 전용 모델 설정
```

### 2. Google Cloud 인증
```bash
gcloud auth application-default login
```

### 3. SSL 인증서 환경 설정 (중요)
실시간 비디오/오디오 통신은 고도로 보안된 연결을 요구합니다. Python의 최신 인증서 목록을 사용하도록 설정해야 합니다.

```bash
# MacOS/Linux
export SSL_CERT_FILE=$(python3 -m certifi)
```

## 예제 실행 방법

### adk web 인터페이스 사용
ADK는 웹 기반의 테스트 인터페이스를 제공합니다.

1. `01-basic` 폴더(최상위)에서 아래 명령어를 실행합니다:
   ```bash
   adk web
   ```
2. 브라우저에서 열린 UI의 에이전트 목록에서 `live`를 선택합니다.
3. 마이크 또는 카메라 접근 권한을 허용하고 실시간으로 에이전트와 대화합니다.

## 기술적 참고 사항
- **SSL_CERT_FILE**: `certifi` 패키지는 신뢰할 수 있는 기관(CA)에서 발급한 인증서 목록을 제공합니다. 이 설정이 없으면 Google 서버와의 보안 연결이 거부될 수 있습니다.
- **지연 시간**: 네트워크 환경에 따라 반응 속도가 달라질 수 있으며, 짧은 지침(Instruction)은 에이전트의 응답 생성 시간을 단축하는 데 도움이 됩니다.

## 라이선스
이 프로젝트는 Apache License 2.0을 따릅니다.