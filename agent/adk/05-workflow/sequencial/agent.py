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

from .sub_agent import positive_critic, negative_critic, review_critic

load_dotenv(dotenv_path="../../.env")

# `root_agent`는 각 하위 에이전트가 순서대로 실행되는 간단한 파이프라인을 정의합니다.
# 이후 단계가 이전 단계에서 생성된 출력에 의존하는 경우 SequentialAgent를 사용하세요.
# 이 파이프라인에서:
#  - `positive_critic`이 먼저 실행되어 긍정적인 비평을 제공합니다.
#  - `negative_critic`이 다음에 실행되어 부정적인 비평을 제공합니다.
#  - `review_critic`이 마지막으로 실행되어 결합된 결과를 검토하고 최종 평가를 생성합니다.
root_agent = SequentialAgent(
    name="pipeline_agent",
    sub_agents=[positive_critic, negative_critic, review_critic],
    description="이것은 에이전트(positive_critic, negative_critic, review_critic)를 순차적으로 실행하는 에이전트입니다.",
)
