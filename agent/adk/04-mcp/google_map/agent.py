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
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioConnectionParams, StdioServerParameters

load_dotenv(dotenv_path="../../.env")

def mcp_google_map():

    """
    환경 변수에서 API 키를 사용하여 MCP Google Maps 도구 세트를 초기화합니다.
    2025년 8월 현재 Google Maps API는 실험적이며 향후 버전에서 예고 없이 변경되거나 제거될 수 있습니다. 언제든지 주요 변경 사항이 도입될 수 있습니다.
    
    """

    # 환경 변수에서 Google Maps API 키 로드
    google_maps_api_key = os.getenv("GOOGLE_MAPS_API_KEY")

    # API 키가 설정되지 않은 경우 예외를 발생시켜 자격 증명 없이 실행되는 것을 방지합니다.
    if not google_maps_api_key:
        raise RuntimeError("GOOGLE_MAPS_API_KEY가 설정되지 않았습니다. 환경 변수로 설정해 주세요.")
    else:
        # Google Maps용 MCPToolset 생성, API 키를 서버 환경에 전달
        mcp_google_map = MCPToolset(
            connection_params=StdioConnectionParams(
                server_params=StdioServerParameters(
                    command='npx',
                    args=[
                        "-y",
                        "@modelcontextprotocol/server-google-maps",
                    ],
                    env={
                        "GOOGLE_MAPS_API_KEY": google_maps_api_key
                    }
                ),
            ),
            # 선택적으로 특정 지도 도구를 필터링할 수 있습니다:
            # tool_filter=['get_directions', 'find_place_by_id']
        )
        return mcp_google_map


mcp_google_map_tool = mcp_google_map()

INSTRUCTION = """
    당신은 Google Maps 도구를 사용하여 지도, 길찾기 및 장소 찾기를 돕는 에이전트입니다.
    사용자가 질문을 하면 'mcp_google_map_tool'을 사용하여 결과를 바탕으로 답변을 제공해야 합니다.
"""

root_agent = LlmAgent(
    model=os.getenv("GOOGLE_GENAI_MODEL"),
    name='Assistant_agent_Google_Map',
    instruction=INSTRUCTION,
    tools=[mcp_google_map_tool]
        
)

