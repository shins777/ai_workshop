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

from google.adk.agents.llm_agent import Agent
from google.adk.agents.remote_a2a_agent import AGENT_CARD_WELL_KNOWN_PATH
from google.adk.agents.remote_a2a_agent import RemoteA2aAgent
from google.genai import types
from google.adk.tools.agent_tool import AgentTool
from google.adk.planners import BuiltInPlanner

from .sub_agent import market_info_agent, summarizer_agent

load_dotenv(dotenv_path="../../../.env")

# Define Remote A2A Agents
agent_exchange_rate = RemoteA2aAgent(
    name="agent_exchange_rate",
    description="외부 API를 통해 환율을 확인하는 데 특화된 에이전트입니다. 두 통화 간의 환율을 효율적으로 결정할 수 있습니다.",
    agent_card=(
        f"http://localhost:8001/a2a/agent_exchange_rate{AGENT_CARD_WELL_KNOWN_PATH}"
    ),
)

# Define Agent Tools
market_info_tool = AgentTool( agent=market_info_agent)
summarizer_tool = AgentTool( agent=summarizer_agent)

# Tool that wraps the Remote A2A Agent
exchange_rate_tool = AgentTool( agent=agent_exchange_rate)

# Define the Root Agent with detailed instructions and workflow rules
root_agent = Agent(
    model=os.getenv("GOOGLE_GENAI_MODEL"),
    name="root_agent",
    instruction="""
    당신은 지능형 오케스트레이터 역할을 하는 마스터 AI 에이전트입니다.

    ## 역할: 사용자 의도를 분석하고 미리 정의된 규칙을 실행하는 오케스트레이터 에이전트입니다.

    ## 주요 지침: 아래 규칙을 순서대로 검토하고 일치하는 첫 번째 규칙을 실행해야 합니다. 규칙에 지정된 도구 시퀀스는 필수이며 변경해서는 안 됩니다.

    ## 도구 정의:
        - @market_info_tool: 일반적인 시장/경제 컨텍스트를 제공합니다.
        - @exchange_rate_tool: 통화 쌍의 현재 환율을 반환합니다.
        - @summarizer_tool: 다른 도구의 출력물을 취합하여 최종 답변을 작성합니다. 항상 마지막으로 호출되어야 합니다.

    ## 규칙 1: 환율
        ### 조건: 사용자가 특정 환율을 묻는 경우.
        ### 실행 단계:
            1. @market_info_tool을 호출하여 경제적 배경 지식을 얻습니다.
            2. @exchange_rate_tool을 호출하고 JSON 출력에서 수치 환율을 추출합니다.
            3. 1단계와 2단계의 출력물을 사용하여 @summarizer_tool을 호출합니다.

    ## 규칙 2: 시장 정보
        ### 조건: 사용자가 일반적인 시장 정보를 묻는 경우.
        ### 실행 단계: @market_info_tool을 호출하고 그 결과를 직접 제공합니다. 다른 도구는 사용하지 마십시오.

    ## 규칙 3: 일반 지식 (대체 방안)
        ### 조건: 쿼리가 규칙 1 또는 규칙 2와 일치하지 않는 경우.
        ### 실행 단계: 내부 지식을 사용하여 직접 답변하십시오. 도구를 사용하지 마십시오.
    """,

    global_instruction=(
        """
            당신은 지능형 오케스트레이터 및 라우터로 기능하도록 설계된 고급 AI 에이전트입니다.
            당신의 전체 목적은 사용자 쿼리에 대한 중앙 의사 결정 단위 역할을 하는 것입니다.
        """
    ),

    tools = [market_info_tool,
             exchange_rate_tool,
             summarizer_tool,
             ],

    # planner=BuiltInPlanner(
    #     thinking_config=types.ThinkingConfig(
    #         include_thoughts=True,
    #     ),
    # ),

    generate_content_config=types.GenerateContentConfig(
        safety_settings=[
            types.SafetySetting(  
                category=types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
                threshold=types.HarmBlockThreshold.OFF,
            ),
        ]
    ),
)
