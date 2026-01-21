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

"""
이 모듈은 에이전트를 사용한 예제 워크플로 구성을 제공합니다.
워크플로에는 조사, 비평, 개선 및 결론 단계가 포함됩니다.
"""

from dotenv import load_dotenv
from google.adk.agents import SequentialAgent
from google.adk.agents import LoopAgent

from .sub_agent import research_agent
from .sub_agent import critic_agent
from .sub_agent import refine_agent
from .sub_agent import conclusion_agent

load_dotenv()

# 루프 워크플로 예제: `critics_loop`는 반복적인 비평 및 개선을 수행합니다.
# 루프는 비평 단계와 개선 단계를 번갈아 가며 출력을 개선합니다.
critics_loop = LoopAgent(
    name="critics_loop",
    sub_agents=[
        critic_agent,
        refine_agent,
    ],
    max_iterations=3  # 비평/개선 루프의 최대 반복 횟수
)

# 루트 에이전트는 워크플로를 일련의 단계로 구성합니다:
# 1) research_agent: 초기 콘텐츠 수집 또는 생성
# 2) critics_loop: 콘텐츠를 반복적으로 비평하고 개선
# 3) conclusion_agent: 개선된 결과를 바탕으로 최종 출력 생성
root_agent = SequentialAgent(
    name="confirmation_agent",
    sub_agents=[
        research_agent, 
        critics_loop,
        conclusion_agent
    ],
    description="조사 에이전트를 실행한 다음 반복적인 비평/개선 루프를 실행하고 마지막으로 결론 에이전트를 실행하는 에이전트입니다.",
)
