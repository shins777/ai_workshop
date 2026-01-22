# Copyright 2025 Google LLC
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

import random

from google.adk.agents.llm_agent import Agent
from google.adk.agents.remote_a2a_agent import AGENT_CARD_WELL_KNOWN_PATH
from google.adk.agents.remote_a2a_agent import RemoteA2aAgent
from google.adk.tools.example_tool import ExampleTool
from google.genai import types


# --- Roll Die Sub-Agent ---
def roll_die(sides: int) -> int:
  """Roll a die and return the rolled result."""
  return random.randint(1, sides)


roll_agent = Agent(
    name="roll_agent",
    description="다양한 크기의 주사위를 굴리는 작업을 처리합니다.",
    instruction="""
      당신은 사용자의 요청에 따라 주사위를 굴리는 책임을 집니다.
      주사위를 굴려달라는 요청을 받으면, 면의 수를 정수로 하여 roll_die 도구를 호출해야 합니다.
    """,
    tools=[roll_die],
    generate_content_config=types.GenerateContentConfig(
        safety_settings=[
            types.SafetySetting(  # avoid false alarm about rolling dice.
                category=types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
                threshold=types.HarmBlockThreshold.OFF,
            ),
        ]
    ),
)


example_tool = ExampleTool([
    {
        "input": {
            "role": "user",
            "parts": [{"text": "Roll a 6-sided die."}],
        },
        "output": [
            {"role": "model", "parts": [{"text": "I rolled a 4 for you."}]}
        ],
    },
    {
        "input": {
            "role": "user",
            "parts": [{"text": "Is 7 a prime number?"}],
        },
        "output": [{
            "role": "model",
            "parts": [{"text": "Yes, 7 is a prime number."}],
        }],
    },
    {
        "input": {
            "role": "user",
            "parts": [{"text": "Roll a 10-sided die and check if it's prime."}],
        },
        "output": [
            {
                "role": "model",
                "parts": [{"text": "I rolled an 8 for you."}],
            },
            {
                "role": "model",
                "parts": [{"text": "8 is not a prime number."}],
            },
        ],
    },
])

prime_agent = RemoteA2aAgent(
    name="prime_agent",
    description="숫자가 소수인지 확인하는 작업을 처리하는 에이전트입니다.",
    agent_card=(
        f"http://localhost:8001/a2a/check_prime_agent{AGENT_CARD_WELL_KNOWN_PATH}"
    ),
)

root_agent = Agent(
    model="gemini-2.0-flash",
    name="root_agent",
    instruction="""
      당신은 주사위를 굴리고 숫자가 소수인지 확인할 수 있는 유용한 도우미입니다.
      주사위 굴리기 작업은 roll_agent에게 위임하고, 소수 확인 작업은 prime_agent에게 위임합니다.
      다음 단계를 따르십시오:
      1. 사용자가 주사위를 굴려달라고 하면 roll_agent에게 위임하십시오.
      2. 사용자가 소수 확인을 요청하면 prime_agent에게 위임하십시오.
      3. 사용자가 주사위를 굴린 후 그 결과가 소수인지 확인해 달라고 하면, 먼저 roll_agent를 호출한 다음 결과를 prime_agent에게 전달하십시오.
      진행하기 전에 항상 결과를 명확히 하십시오.
    """,
    global_instruction=(
        "당신은 주사위를 굴리고 소수를 확인할 준비가 된 DicePrimeBot입니다."
    ),
    sub_agents=[roll_agent, prime_agent],
    tools=[example_tool],
    generate_content_config=types.GenerateContentConfig(
        safety_settings=[
            types.SafetySetting(  # avoid false alarm about rolling dice.
                category=types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
                threshold=types.HarmBlockThreshold.OFF,
            ),
        ]
    ),
)
