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
from google.adk.tools import preload_memory_tool 
from google.adk.tools import google_search

load_dotenv()

#--------------------------------[build_search_agent]----------------------------------

search_agent = Agent(
    name = "search_agent",
    model = os.getenv("GOOGLE_GENAI_MODEL"),
    description = "사용자 쿼리에 답변하는 에이전트",
    instruction = """
        당신은 사용자 질문에 답변을 제공하는 에이전트입니다.
        # 사용자가 질문을 제출하면, 해당 질문에 대해 Google 검색(tool: google_search)을 수행하고
        # 그 결과를 바탕으로 답변을 제공하세요. 
        """,
    # tools=[google_search],
    tools=[preload_memory_tool.PreloadMemoryTool()],
)

#--------------------------------[build_recall_agent]----------------------------------

RECALL_INSTRUCTION = """
    당신은 사용자 질문에 답변을 제공하는 에이전트입니다.
    사용자가 이전 대화의 정보를 요청하면, 등록된 도구를 사용하여
    저장된 기억을 검색하고 그 기억을 바탕으로 사용자에게 답변하세요.
"""

recall_agent = Agent(
    name = "recall_agent",
    model = os.getenv("GOOGLE_GENAI_MODEL"),
    description = "메모리에서 정보를 검색하여 사용자 질문에 답변하는 에이전트",
    instruction = """
        당신은 사용자 질문에 답변을 제공하는 에이전트입니다.
        사용자가 이전 대화의 정보를 요청하면, 등록된 도구를 사용하여
        저장된 기억을 검색하고 그 기억을 바탕으로 사용자에게 답변하세요.""",
    tools=[preload_memory_tool.PreloadMemoryTool()],
)
