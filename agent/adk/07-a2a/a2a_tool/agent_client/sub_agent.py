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

from google.adk.agents.llm_agent import Agent
from google.adk.tools import google_search
from google.genai import types
import os 

market_info_agent = Agent(
    name="market_info_agent",
    model=os.getenv("GOOGLE_GENAI_MODEL"),
    description="구글 검색을 통해 현재 경제 정보를 제공할 수 있는 에이전트입니다.",
    instruction="""
        당신은 구글 검색을 통해 현재 경제 정보를 제공하는 유용한 도우미입니다.
        
        ## 역할: 실시간 경제 정보 전문 AI 어시스턴트.
        ## 작업: 경제에 대해 질문을 받으면 반드시 `@google_search` 도구를 사용하여 가장 최신의 관련 뉴스, 트렌드 및 데이터를 찾아야 합니다.
        ## 제약 사항: 모든 답변은 `@google_search` 도구의 실시간 결과를 기반으로 해야 합니다. 내부 지식을 사용하지 마십시오.
    """,

    tools=[google_search],

    generate_content_config=types.GenerateContentConfig(
        safety_settings=[
            types.SafetySetting(  
                category=types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
                threshold=types.HarmBlockThreshold.OFF,
            ),
        ]
    ),
)


summarizer_agent = Agent(
    name="summarizer_agent",
    model=os.getenv("GOOGLE_GENAI_MODEL"),
    description="다른 에이전트와 도구로부터 받은 정보를 요약할 수 있는 에이전트입니다.",
    instruction="""
      당신은 다른 에이전트나 도구로부터 받은 정보를 요약하는 유용한 도우미입니다.
      
      ## 역할: 도구 출력물을 취합하는 포맷팅 에이전트.

      ## 포맷:
        ### 시장 요약
        [여기에 @market_info_tool의 현재 시장 요약 삽입]

        ### 시장 분석 및 인사이트
        [여기에 @market_info_tool의 현재 시장 분석 결과 삽입]

        ### 환율 정보:
        [여기에 @exchange_rate_tool의 전체 출력물 삽입]
    """,
)    