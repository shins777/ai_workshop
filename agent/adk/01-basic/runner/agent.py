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

load_dotenv(dotenv_path="../../.env")

#--------------------------------[positive_critic]----------------------------------
positive_critic = Agent(
    name = "positive_critic",
    model = os.getenv("GOOGLE_GENAI_MODEL"),
    description = "사용자의 질문에 대해 긍정적인 면만 답변하는 에이전트입니다.",
    instruction = """당신은 사용자 문의 주제에 대해 긍정적인 리뷰를 작성하는 에이전트입니다. 
                      답변을 제공할 때는 가능한 간결하고 명확하게 작성하며, 항상 "긍정적인 리뷰 결과:"라는 문구로 시작하세요. """,

)    

#--------------------------------[negative_critic]----------------------------------
negative_critic = Agent(
    name = "negative_critic",
    model = os.getenv("GOOGLE_GENAI_MODEL"),
    description = "사용자의 질문에 대해 부정적인 면만 답변하는 에이전트입니다.",
    instruction = """당신은 사용자 질문의 주제에 대해 부정적인 리뷰를 작성하는 에이전트입니다.
                      답변을 제공할 때는 가능한 간결하고 명확하게 작성하며, 항상 "부정적인 리뷰 결과:"라는 문구로 시작하세요. """,
)    

#--------------------------------[root_agent]----------------------------------

INSTRUCTION = """
당신은 사용자의 질문에 답변하는 도움을 주는 에이전트입니다.
다음과 같이 하위 에이전트나 도구를 사용하여 답변을 제공합니다:

하위 에이전트:
1. 사용자가 긍정적인 리뷰를 요청하면 positive_critic 에이전트를 사용하세요.
2. 사용자가 부정적인 리뷰를 요청하면 negative_critic 에이전트를 사용하세요.

만일 root_agent가 답변할 때는 "## 일반적인 질문에 대한 Root Agent의 답변 ## "로 시작하여 답변해주세요.
 
"""

root_agent = Agent(
    name = "root_agent",
    model = os.getenv("GOOGLE_GENAI_MODEL"),
    description = "사용자의 질문에 답변하는 에이전트",
    instruction = INSTRUCTION,
    sub_agents = [positive_critic, negative_critic],
)
