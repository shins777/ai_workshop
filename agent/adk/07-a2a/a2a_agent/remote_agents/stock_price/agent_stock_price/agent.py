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

from google.adk import Agent
from google.genai import types
from google.adk.tools.agent_tool import AgentTool

from .sub_agents import company_info_agent, summarizer_agent
from .functions import get_stock_price

# Make the sub-agents into tools
company_info_tool = AgentTool( agent=company_info_agent)
summarizer_tool = AgentTool( agent=summarizer_agent)

# Define root agent as an orchestrator
root_agent = Agent(
    model=os.getenv("GOOGLE_GENAI_MODEL"),
    name='company_stock_price_agent',
    description="회사의 정보와 주식 가격을 제공하는 데 특화된 에이전트입니다.",
    instruction="""

        당신은 회사의 주가와 최신 뉴스를 포함한 포괄적인 정보를 제공하는 오케스트레이터 에이전트입니다.
        
        ## 목표 : 주어진 회사 심볼에 대한 주가와 최신 뉴스를 제공합니다.

        ## 실행 단계:
            1. @get_stock_price 도구를 사용하여 주가를 가져옵니다.
            2. @company_info_tool을 사용하여 최신 뉴스를 찾습니다.
            3. 필수 사항: 최종 답변을 생성하기 위해 1단계와 2단계의 출력물 모두를 사용하여 @summarizer_tool을 호출하십시오.
        
        ## 제약 사항: 미리 학습된 지식을 사용하지 마십시오. 도구 출력물에만 의존하십시오.

    """,
    
    tools=[
        get_stock_price,
        company_info_tool, 
        summarizer_tool        
    ],

    generate_content_config=types.GenerateContentConfig(
        safety_settings=[
            types.SafetySetting(  
                category=types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
                threshold=types.HarmBlockThreshold.OFF,
            ),
        ]
    ),
)
