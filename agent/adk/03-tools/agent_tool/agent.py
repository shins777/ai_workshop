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
from google.adk.tools.agent_tool import AgentTool

from .sub_agent import positive_critic, negative_critic

load_dotenv(dotenv_path="../../.env")

INSTRUCTION = """
    당신은 사용자의 질문에 답변하는 에이전트입니다.
    사용자의 질문에 따라 다음 도구를 사용하여 답변을 제공해야 합니다:
    - 사용자가 긍정적인 비평을 요청하면 positive_critic 도구를 사용하여 긍정적인 비평을 작성하세요.
    - 사용자가 부정적인 비평을 요청하면 negative_critic 도구를 사용하여 부정적인 비평을 작성하세요.
    - 사용자가 긍정적인 비평과 부정적인 비평을 모두 요청하면 두 도구(positive_critic 및 negative_critic)를 모두 사용하여 각각의 비평을 작성하세요.
    - 사용자가 일반적인 질문을 하면 root_agent가 직접 답변하세요.
        
    """

root_agent = Agent(
    name = "root_agent",
    model = os.getenv("GOOGLE_GENAI_MODEL"),
    description = "사용자의 질문에 답변하는 에이전트",
    instruction = INSTRUCTION,
    tools = [AgentTool(agent=positive_critic),
            AgentTool(agent=negative_critic)]
)
