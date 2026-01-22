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

from dotenv import load_dotenv
from google.adk.agents import SequentialAgent
from google.adk.agents import ParallelAgent

from .sub_agent import positive_critic, negative_critic, review_critic

load_dotenv(dotenv_path="../../.env")

# `parallel_research_agent`는 여러 연구 스타일의 하위 에이전트(positive_critic 및 negative_critic)를
# 동시에 실행하여 다양한 관점이나 데이터를 병렬로 수집합니다.
# 독립적인 하위 작업을 동시에 실행하여 정보 수집 속도를 높이려면 ParallelAgent를 사용하세요.
parallel_research_agent = ParallelAgent(
    name="parallel_research_agent",
    sub_agents=[positive_critic, negative_critic],
    description="여러 연구 에이전트를 병렬로 실행하여 정보를 수집하는 에이전트입니다."
)

# `root_agent`는 간단한 파이프라인을 구성합니다. 먼저 병렬 연구 단계를 실행한 다음
# 검토/비평 에이전트를 실행합니다. SequentialAgent는 sub_agents의 순차적 실행을 강제하므로
# 이후 단계는 이전 단계의 출력에 의존할 수 있습니다.
root_agent = SequentialAgent(
    name="pipeline_agent",
    sub_agents=[parallel_research_agent, review_critic],
    description="parallel_research_agent와 review_critic을 순차적으로 실행하는 에이전트입니다.",
)
