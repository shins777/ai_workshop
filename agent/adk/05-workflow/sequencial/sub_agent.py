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
from google.adk.tools import google_search

load_dotenv()

#--------------------------------[positive_critic]----------------------------------
positive_critic = Agent(
    name = "positive_critic",
    model = os.getenv("GOOGLE_GENAI_MODEL"),
    description = "사용자 질문의 긍정적인 측면만 답변하는 에이전트입니다.",
    instruction = """당신은 사용자 문의 주제에 대해 긍정적인 리뷰를 작성하는 에이전트입니다. 
                     응답을 제공할 때 가능한 한 간결하고 명확하게 3줄로 작성해야 합니다.
                      그리고 항상 "긍정적 리뷰 결과:"라는 문구로 시작하세요. """,
    tools=[google_search],
    output_key="positive_critic_output",                      
)    

#--------------------------------[negative_critic]----------------------------------
negative_critic = Agent(
    name = "negative_critic",
    model = os.getenv("GOOGLE_GENAI_MODEL"),
    description = "사용자 질문의 부정적인 측면만 답변하는 에이전트입니다.",
    instruction = """당신은 사용자 질문 주제에 대해 부정적인 리뷰를 작성하는 에이전트입니다.
                     응답을 제공할 때 가능한 한 간결하고 명확하게 3줄로 작성해야 합니다.
                      그리고 항상 "부정적 리뷰 결과:"라는 문구로 시작하세요. """,
    tools=[google_search],
    output_key="negative_critic_output",                       
)    

#--------------------------------[review_critic]----------------------------------
review_critic = Agent(
    name = "review_critic",
    model = os.getenv("GOOGLE_GENAI_MODEL"),
    description = "사용자 질문의 긍정적 측면과 부정적 측면을 검토하고 전반적으로 요약하는 에이전트입니다.",
    instruction = f"""
            당신은 주어진 주제에 대한 긍정적 비판과 부정적 비판을 바탕으로 최종 요약 및 결론을 제공하는 에이전트입니다.
            응답은 다음 두 가지 정보를 기반으로 해야 합니다:

            * 긍정적 측면: ```{{positive_critic_output}}```
            * 부정적 측면: ```{{negative_critic_output}}```

            응답할 때 항상 ### 최종 요약: 이라고 명시하세요.
            응답을 제공할 때 가능한 한 간결하고 명확하게 3줄로 작성해야 합니다.
   
        """,
)  
