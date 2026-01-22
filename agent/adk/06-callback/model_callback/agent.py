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

from callback import callback_before_model
from callback import callback_after_model

load_dotenv(dotenv_path="../../.env")

INSTRUCTION = """
    당신은 사용자의 질문에 답변하는 AI 에이전트입니다.
    답변을 제공할 때는 아래와 같은 구조로 간결하고 명확하게 작성해 주세요:
        - 질문 내용:
        - 질문 의도:
        - 답변 내용:
    참고: 일상적인 대화성 질문에는 별도의 형식 없이 자연스럽게 답변하세요.  
    """

root_agent = Agent(
    name = "root_agent",
    model = os.getenv("GOOGLE_GENAI_MODEL"),
    description = "사용자 문의에 대해 답변하는 에이전트입니다.",
    instruction = INSTRUCTION,
    before_model_callback=callback_before_model,
    after_model_callback=callback_after_model 
)