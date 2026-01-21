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
from google.adk.code_executors import BuiltInCodeExecutor

load_dotenv()

INSTRUCTION = """
        당신은 프로그램 코드를 실행하여 계산을 수행하고 결과를 반환하는 에이전트입니다.
        사용자가 수학적 표현을 입력하면 Python 코드를 작성하여 표현을 계산하고 내장된 코드 실행기를 통해 실행합니다.
        """

root_agent = Agent(
    name = "code_execution_agent",
    model = os.getenv("GOOGLE_GENAI_MODEL"),
    description = "프로그램 코드를 실행하여 계산을 수행하고 결과를 반환하는 에이전트입니다.",
    instruction = INSTRUCTION,
    code_executor=BuiltInCodeExecutor(),   
)   
