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
from google.adk.agents import Agent
from toolbox_core import ToolboxSyncClient

load_dotenv(dotenv_path="../../.env")

def get_toolbox():
    """
    ToolboxSyncClient 인스턴스를 생성하고 구성합니다.
    이 함수는 환경 변수를 로드하고 ToolboxSyncClient를 초기화합니다.
    클라이언트는 툴박스와의 동기화를 관리하는 데 사용됩니다.

    Returns:
        ToolboxSyncClient: 툴박스와의 동기화를 관리할 준비가 된 클라이언트 인스턴스입니다.
    """
    toolbox = ToolboxSyncClient(    
        os.getenv("TOOLBOX_SYNC_CLIENT"),
    )

    tool_set = toolbox.load_toolset('my_bq_toolset')
    print(f"Toolbox set: {tool_set}")
    
    tools = toolbox.load_tool('query_bbc'),
    print(f"Toolbox tools: {tools}")
    
    return tools

tools = get_toolbox()

INSTRUCTION = """
    당신은 사용자 질문에 답변을 제공하는 에이전트입니다.
    사용자가 질문을 하면 관련 도구를 사용하여 답변을 생성해야 합니다.

"""

root_agent = Agent(
    name = "search_agent",
    model = os.getenv("GOOGLE_GENAI_MODEL"),
    description = "사용자 쿼리에 답변하는 에이전트",
    instruction = INSTRUCTION,
    tools=tools,
)
