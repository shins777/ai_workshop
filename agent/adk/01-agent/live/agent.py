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

load_dotenv()

INSTRUCTION = """
    당신은 사용자의 질문에 답변하는 에이전트입니다.
    가능하면 짧은 문장으로 답변해야 합니다.
"""

root_agent = Agent(
    name = "basic_agent",
    model = os.getenv("GOOGLE_GENAI_LIVE_MODEL"),
    description = "사용자의 질문에 답변하는 에이전트",
    instruction = INSTRUCTION,
)
