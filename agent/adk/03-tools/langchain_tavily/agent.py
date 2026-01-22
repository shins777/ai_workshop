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

from google.adk.tools.langchain_tool import LangchainTool
from langchain_community.tools import TavilySearchResults

from . import function

load_dotenv(dotenv_path="../../.env")

# Instantiate the LangChain tool
tavily_tool_instance = TavilySearchResults(
    max_results=5,
    search_depth="advanced",
    include_answer=True,
    include_raw_content=True,
    include_images=True,
)

# Wrap it with LangchainTool for ADK
adk_tavily_tool = LangchainTool(tool=tavily_tool_instance)

INSTRUCTION = """
    당신은 환율 및 웹 검색 정보에 대해 검색하고 답변하는 AI 에이전트입니다.
    1. 환율 검색
        기준 통화와 대상 통화가 주어지면 지정된 날짜의 환율 정보를 제공하세요.
        질문에서 기준 통화, 대상 통화, 날짜를 추출하고 'get_exchange_rate' 도구를 사용하여 검색하세요.
        답변 형식:
        - 기준 통화: USD
        - 대상 통화: KRW
        - 날짜: 2025-05-20
        - 환율: 1400
    
    2. 질문이 환율에 관한 것이 아니고 웹 검색이 필요한 경우 아래의 adk_tavily_tool을 사용하여 검색하세요.
    답변을 제공할 때는 다음 형식을 엄격히 준수해야 합니다:

        - 질문에 대한 이해
        - 검색 결과 전체 요약:
        - 검색 출처별 요약:

"""

root_agent = Agent(
    name = "root_agent",
    model = os.getenv("GOOGLE_GENAI_MODEL"),
    description = "사용자 쿼리에 대한 질문에 답변하는 에이전트",
    instruction = INSTRUCTION,
    tools=[adk_tavily_tool, function.get_exchange_rate]
)
