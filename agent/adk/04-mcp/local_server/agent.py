# Copyright 2025 Forusone(shins777@gmail.com)
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

load_dotenv(dotenv_path="../../.env")

def mcp_toolset():
    """
    MCP(Model Context Protocol)를 사용하여 환율 작업을 위한 MCPToolset을 생성하고 구성합니다.
    이 함수는 지정된 명령과 인수를 사용하여 사용자 지정 환율 서버에 연결하는 MCPToolset 인스턴스를 설정합니다. 이를 통해 에이전트가 환율 정보를 쿼리할 수 있습니다.

    Returns:
        MCPToolset: 환율 작업을 위해 구성된 MCPToolset 인스턴스.
    """

    mcp_toolset = MCPToolset(
            connection_params=StdioServerParameters(
                command='python3', 
                args=[
                      "-m"
                      "local_server.exchange_rate"
                      ],
            )
    )    
            
            
    return mcp_toolset

INSTRUCTION = """
    당신은 사용자 질문에 답변을 제공하는 에이전트입니다.
    사용자가 특정 통화에 대한 환율을 물러보면 'exchange_rate_tool'을 사용하여 결과를 바탕으로 답변을 제공해야 합니다.
"""

exchange_rate_tool = mcp_toolset()

root_agent = LlmAgent(
    name = "Exchange_Rate_Agent",
    model = os.getenv("GOOGLE_GENAI_MODEL"),
    description = "환율에 대해 답변하는 에이전트",
    instruction = INSTRUCTION,
    tools=[exchange_rate_tool],
)
