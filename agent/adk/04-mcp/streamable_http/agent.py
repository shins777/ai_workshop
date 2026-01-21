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
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StreamableHTTPConnectionParams

load_dotenv()

def mcp_streamable_http_tool():
    """
    원격 MCP Streamable HTTP 서버에 연결하는 MCPToolset을 생성하고 구성합니다.

    이 헬퍼는 제공된 서비스 URL과 함께 StreamableHTTPConnectionParams를 사용하여 MCPToolset을 구성합니다.
    반환된 도구 세트는 LLM 에이전트가 Streamable HTTP 서버에 의해 노출된 원격 MCP 도구를 호출하는 데 사용할 수 있습니다.

    Returns:
        MCPToolset: Streamable HTTP 연결 매개변수를 사용하여 구성된 MCPToolset 인스턴스.
    """

    mcp_toolset = MCPToolset(
        connection_params=StreamableHTTPConnectionParams(
            url="https://mcp-streamable-http-721521243942.us-central1.run.app/mcp/",
        ),
    )
            
    return mcp_toolset

INSTRUCTION = """
    당신은 사용자 질문에 답변을 제공하는 에이전트입니다.
    사용자가 환율과 관련된 질문을 하면 'get_exchange_rate'를 사용하여 결과를 바탕으로 답변을 제공해야 합니다.
"""

get_exchange_rate = mcp_streamable_http_tool()

root_agent = LlmAgent(
    name = "get_exchange_rate_agent",
    model = os.getenv("GOOGLE_GENAI_MODEL"),
    description = "사용자 쿼리에 대해 답변하는 에이전트",
    instruction = INSTRUCTION,
    tools=[get_exchange_rate],
)
