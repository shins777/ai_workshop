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

from .sub_agent import positive_critic
from .sub_agent import negative_critic
from .sub_agent import review_critic

from .critic import CriticAgent

load_dotenv(dotenv_path="../../.env")

# 모듈 목적:
# 이 모듈은 세 가지 하위 에이전트를 구성하는 사용자 지정 CriticAgent를 정의합니다.
# - positive_critic_agent: 긍정적인 피드백을 생성하고 강점을 강조합니다.
# - negative_critic_agent: 건설적인 부정적인 피드백 또는 약점을 생성합니다.
# - review_critic_agent: 비평을 집계하고 최종 검토를 생성합니다.
#
# CriticAgent는 이러한 하위 에이전트를 조정하여 구조화된 비평을 생성하고
# 주어진 입력 또는 문서에 대한 전체 평가를 제공합니다.

root_agent = CriticAgent(
    name = "critic_agent",
    positive_critic_agent = positive_critic,
    negative_critic_agent = negative_critic,
    review_critic_agent = review_critic,        
)

# `root_agent`는 ADK 런타임에서 직접 사용하거나
# 결합된 비평 및 검토가 필요한 상위 수준 워크플로에 연결할 수 있습니다.
