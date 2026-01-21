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
from google.adk.tools import google_search

load_dotenv()


INSTRUCTION = """
    당신은 사용자 질문에 답변을 제공하는 에이전트입니다.
    사용자가 질문을 입력하면 Google 검색(tool:google_search)을 수행하고 결과를 바탕으로 답변을 제공해야 합니다. 모든 답변은 간결하고 명확해야 하며, 사용자 질문과 동일한 언어로 작성되어야 합니다.

    답변을 제공할 때는 다음 형식을 엄격히 준수해야 합니다:

    1. 질문에 대한 이해
    2. 검색 결과 전체 요약:
    3. 검색 출처별 요약:

"""

root_agent = Agent(
    name = "search_agent",
    model = os.getenv("GOOGLE_GENAI_MODEL"),
    description = "사용자 쿼리에 답변하는 에이전트",
    instruction = INSTRUCTION,
    tools=[google_search],
)
