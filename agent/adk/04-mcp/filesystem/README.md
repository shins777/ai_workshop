# ADK MCP 파일 시스템 도구 예제 (04-mcp/filesystem)

이 예제는 **Model Context Protocol (MCP)**을 사용하여 에이전트가 로컬 파일 시스템의 파일과 디렉토리를 관리할 수 있도록 하는 방법을 보여줍니다.

## 주요 개념

- **MCP Filesystem Server**: `@modelcontextprotocol/server-filesystem` 패키지를 사용하여 표준화된 방식으로 파일 작업을 수행합니다.
- **Stdio 전송**: 에이전트와 MCP 서버는 표준 입출력(stdio)을 통해 통신합니다.

## 주요 구성 요소

### 1. 에이전트 정의 (`agent.py`)
- **`mcp_toolset` 함수**: `npx`를 통해 MCP 서버를 실행하고, 에이전트가 접근할 수 있는 절대 경로를 인자로 전달하여 `MCPToolset`을 생성합니다.
- **`file_system_toolset`**: `list_directory`, `read_file`, `write_file` 등 파일 시스템 관리에 필요한 도구들을 자동으로 포함합니다.
- **`root_agent`**: 정의된 `file_system_toolset`을 도구로 사용하여 사용자의 파일 관리 요청을 수행합니다.

## 사전 준비 사항

- **Node.js**: `npx` 명령어를 사용하기 위해 Node.js가 설치되어 있어야 합니다.
- **권한**: 에이전트가 접근하려는 대상 폴더에 대한 읽기/쓰기 권한이 필요합니다.

## 실행 방법

1. `04-mcp/filesystem/agent.py` 파일 내의 `target_folder_path`가 에이전트가 관리할 실제 절대 경로로 설정되어 있는지 확인합니다.
2. `04-mcp` 폴더에서 `adk web`을 실행합니다.
3. 에이전트 목록에서 `filesystem`을 선택하여 다음과 같은 질문을 테스트합니다:
   - "현재 폴더에 있는 파일 목록을 알려줘."
   - "`test.txt` 파일을 가상의 내용으로 생성해줘."

## 기술적 참고 사항
- MCP 서버를 실행할 때 전달되는 경로는 반드시 **절대 경로(Absolute Path)**여야 합니다.
- `MCPToolset`에서 `tool_filter` 옵션을 사용하면 에이전트가 사용할 수 있는 도구를 제한하여 보안을 강화할 수 있습니다.

## 라이선스
이 프로젝트는 Apache License 2.0을 따릅니다.