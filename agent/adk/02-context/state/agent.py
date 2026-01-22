import os
from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.tools import google_search

load_dotenv(dotenv_path="../../.env")

INSTRUCTION = """
    당신은 사용자 질문에 답변을 제공하는 에이전트입니다.
    사용자가 질문을 제출하면, 해당 질문에 대해 Google 검색(tool: google_search)을 수행하고
    그 결과를 바탕으로 답변을 제공하세요.
"""

root_agent = Agent(
    name = "search_agent",
    model = os.getenv("GOOGLE_GENAI_MODEL"),
    description = "사용자 쿼리에 답변하는 에이전트",
    instruction = INSTRUCTION,
    tools=[google_search],
    output_key = "last_turn"
)

