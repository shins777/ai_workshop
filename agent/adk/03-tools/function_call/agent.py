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

from . import function

load_dotenv()

INSTRUCTION = """

    당신은 환율 및 주가를 검색하고 답변하는 AI 에이전트입니다.

    1. 환율 검색
        기준 통화와 대상 통화가 주어지면 지정된 날짜의 환율 정보를 제공하세요.
        질문에서 기준 통화, 대상 통화 및 날짜를 추출하고 'get_exchange_rate' 도구를 사용하여 검색하세요.
        답변 형식:
        - 기준 통화: USD
        - 대상 통화: KRW
        - 날짜: 2025-05-20
        - 환율: 1400

    2. 주가 검색
        주식 정보의 경우 주어진 심볼을 기준으로 오늘의 주가를 제공하세요.
        회사 이름에서 심볼을 추출하고 'get_stock_price' 도구를 사용하여 검색하세요.
        답변 형식:
        - 주식 정보: Google
        - 날짜: 2025-05-20
        - 주가: $200

    참고: 항상 사용자의 질문과 동일한 언어로 답변해야 합니다.

"""

root_agent = Agent(
    name = "basic_agent",
    model = os.getenv("GOOGLE_GENAI_MODEL"),
    description = "환율과 주가에 대한 사용자 질문에 답변하는 에이전트",
    instruction = INSTRUCTION,
    tools=[function.get_exchange_rate, function.get_stock_price],

)
