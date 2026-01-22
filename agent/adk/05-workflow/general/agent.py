# Copyright 2025 Forusone(forusone777@gmail.com)
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

from .sub_agent import positive_critic, negative_critic

load_dotenv(dotenv_path="../../.env")

SYSTEM_INSTRUCTION = """
    당신은 사용자의 다양한 질문에 충실하게 답변하는 에이전트입니다.
"""

INSTRUCTION = """
    당신은 사용자 질문에 답변을 제공하는 에이전트입니다.
    응답을 작성할 때 아래 흐름을 따르세요:
        1. 사용자가 질문을 제출하면 먼저 사용자의 의도를 요약합니다. 요약은 "질문 의도:"라는 문구로 시작하고 그 뒤에 의도를 적습니다.
        2. 사용자의 요청에 따라 다음과 같이 하위 에이전트를 사용하여 응답을 생성합니다:
            - 사용자가 긍정적인 비평을 요청하면 `positive_critic` 하위 에이전트를 사용합니다.
            - 사용자가 부정적인 비평을 요청하면 `negative_critic` 하위 에이전트를 사용합니다.
"""

root_agent = Agent(
    name = "Search_agent",  
    model = os.getenv("GOOGLE_GENAI_MODEL"),
    description = "사용자 검색어에 응답하는 에이전트입니다.",
    global_instruction = SYSTEM_INSTRUCTION,
    instruction = INSTRUCTION,
    sub_agents = [positive_critic, negative_critic],
)
