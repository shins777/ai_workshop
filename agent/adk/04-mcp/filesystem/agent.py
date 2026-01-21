# Copyright 2025 Forusone(forusone777@gmail.com)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from dotenv import load_dotenv
from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters

load_dotenv()

def mcp_toolset(target_folder_path: str):
    """
    MCP(Model Context Protocol)를 통한 파일 시스템 작업을 위한 MCPToolset을 생성하고 구성합니다.
    이 함수는 주어진 대상 폴더 경로를 사용하여 MCPToolset 인스턴스를 설정하여,
    에이전트가 MCP 서버를 통해 파일 시스템과 상호 작용할 수 있도록 합니다.
    서버는 npx 및 @modelcontextprotocol/server-filesystem 패키지를 사용하여 연결하도록 구성됩니다.

    Args:
        target_folder_path (str): 파일 시스템 작업을 위한 대상 폴더의 절대 경로

    Returns:
        MCPToolset: 파일 관리 작업을 위해 구성된 MCPToolset 인스턴스
    """

    file_system_toolset = MCPToolset(
                connection_params=StdioServerParameters(
                    command='npx',
                    args=[
                        "-y",  # Argument for npx to auto-confirm install
                        "@modelcontextprotocol/server-filesystem",
                        # IMPORTANT: This MUST be an ABSOLUTE path to a folder the
                        # npx process can access.
                        # Replace with a valid absolute path on your system.
                        # For example: "/Users/youruser/accessible_mcp_files"
                        # or use a dynamically constructed absolute path:
                        os.path.abspath(target_folder_path),
                    ],
                ),
                # Optional: Filter which tools from the MCP server are exposed
                # tool_filter=['list_directory', 'read_file']
            )
    return file_system_toolset


INSTRUCTION = """
    당신은 주어진 폴더 내의 파일을 관리하는 것을 돕는 에이전트입니다.
    사용자가 질문을 입력하면 'file_system_toolset'을 사용하여 결과를 바탕으로 답변을 제공해야 합니다.
"""

target_folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "/")
file_system_toolset = mcp_toolset(target_folder_path=target_folder_path)

root_agent = LlmAgent(
    name = "search_agent",
    model = os.getenv("GOOGLE_GENAI_MODEL"),
    description = "사용자 쿼리에 대해 답변하는 에이전트",
    instruction = INSTRUCTION,
    tools=[file_system_toolset],
)