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

from dotenv import load_dotenv

from google.adk.agents.llm_agent import Agent
from google.adk.agents.remote_a2a_agent import AGENT_CARD_WELL_KNOWN_PATH
from google.adk.agents.remote_a2a_agent import RemoteA2aAgent
from google.genai import types
from google.adk.planners import BuiltInPlanner

import os

load_dotenv(dotenv_path="../../../.env")

agent_stock_price = RemoteA2aAgent(
    name="agent_stock_price",
    description="외부 API를 통해 주식 가격을 확인하는 데 특화된 에이전트입니다. 주어진 회사 심볼의 현재 주가를 효율적으로 파악할 수 있습니다.",
    agent_card=(
        f"http://localhost:8001/a2a/agent_stock_price{AGENT_CARD_WELL_KNOWN_PATH}"

    ),
)

root_agent = Agent(
    model=os.getenv("GOOGLE_GENAI_MODEL"),
    name="root_agent",
    instruction="""

    당신은 지능형 오케스트레이터 역할을 하는 마스터 AI 에이전트입니다.
    당신의 주요 목표는 사용자 쿼리를 분석하고 이를 올바른 도구 또는 서브 에이전트로 효율적으로 라우팅하여 포괄적이고 정확한 답변을 생성하는 것입니다.

    ## 도구 및 서브 에이전트 정의
    -   `@agent_stock_price`: 주어진 회사 심볼을 받아 해당 회사의 현재 주가를 반환하는 원격 서브 에이전트입니다.
    
    ## 핵심 원칙
    - 다음 규칙 중 하나라도 일치하는 경우, 쿼리에 답변하기 위해 이미 학습된 정보를 사용해서는 안 됩니다.
    - 대신, 정의된 도구와 서브 에이전트를 통해 가져온 실시간 데이터에만 전적으로 의존해야 합니다.

    ## 워크플로우 및 라우팅 규칙
        
    **규칙 1: 환율 문의**
    -   **조건:** 사용자의 주된 의도가 환율을 묻는 것인 경우.
    -   **실행 계획 단계:**
        `@agent_stock_price` 서브 에이전트를 호출하여 주어진 회사 심볼을 전달하고 현재 주가를 가져와야 합니다. (참고: 이 예제에서는 환율 문의 시 주가 에이전트를 호출하도록 설정되어 있습니다.)

    **규칙 2: 일반 지식 문의 (대체 방안)**
    -   **조건:** 쿼리가 위의 어떤 규칙과도 일치하지 않는 경우.
    -   **실행 계획:**
        1. 내부 지식을 사용하여 직접 답변하십시오.
        
    **전체 출력 형식:** 간결하고 명확한 답변을 제공하십시오.

    """,

    global_instruction=(
        """
            당신은 지능형 오케스트레이터 및 라우터로 기능하도록 설계된 고급 AI 에이전트입니다.
            당신의 전체 목적은 사용자 쿼리에 대한 중앙 의사 결정 단위 역할을 하는 것입니다.
        """
    ),

    sub_agents=[agent_stock_price],

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
