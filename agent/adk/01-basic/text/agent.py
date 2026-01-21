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

load_dotenv(dotenv_path="../../.env")

INSTRUCTION = """
당신은 사용자의 질문에 답변하는 AI 에이전트입니다.
답변을 제공할 때는 질문에 대한 이해한 내용을 설명하고 간결하고 명확하게 답변하세요.
"""

root_agent = Agent(
    name = "basic_agent",
    model = os.getenv("GOOGLE_GENAI_MODEL"),
    description = "사용자의 질문에 답변하는 에이전트",
    instruction = INSTRUCTION,
    tools=[google_search],

)
