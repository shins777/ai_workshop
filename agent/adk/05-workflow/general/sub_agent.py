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

load_dotenv()

#--------------------------------[positive_critic]----------------------------------
positive_critic = Agent(
    name = "positive_critic",
    model = os.getenv("GOOGLE_GENAI_MODEL"),
    description = "사용자 질문의 긍정적인 측면만 답변하는 에이전트입니다.",
    instruction = """당신은 사용자 문의 주제에 대해 긍정적인 리뷰를 작성하는 에이전트입니다. 
                      응답을 제공할 때 가능한 한 간결하고 명확하게 작성해야 하며, 항상 "긍정적 리뷰 결과:"라는 문구로 시작하세요. """,
    output_key="positive_critic_output",
)    

#--------------------------------[negative_critic]----------------------------------
negative_critic = Agent(
    name = "negative_critic",
    model = os.getenv("GOOGLE_GENAI_MODEL"),
    description = "사용자 질문의 부정적인 측면만 답변하는 에이전트입니다.",
    instruction = """당신은 사용자 질문 주제에 대해 부정적인 리뷰를 작성하는 에이전트입니다.
                      응답을 제공할 때 가능한 한 간결하고 명확하게 작성해야 하며, 항상 "부정적 리뷰 결과:"라는 문구로 시작하세요. """,
    output_key="negative_critic_output",                      
)    