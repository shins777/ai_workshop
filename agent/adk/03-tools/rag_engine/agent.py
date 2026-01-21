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
from google.adk.tools.retrieval.vertex_ai_rag_retrieval import VertexAiRagRetrieval
from vertexai.preview import rag

load_dotenv()

def buid_rag_tool():
    
    rag_engine_tool = VertexAiRagRetrieval(
        name='retrieve_rag_documentation',
        description=(
            'RAG Engine 코퍼스의 질문과 관련된 문서 및 참조를 검색하려면 이 도구를 사용하세요.'
        ),
        rag_resources=[
            rag.RagResource(
                rag_corpus=os.environ.get("RAG_CORPUS")
            )
        ],
        similarity_top_k=10,
        vector_distance_threshold=0.3,
    )
    return rag_engine_tool

INSTRUCTION = """
    당신은 사용자 질문에 답변을 제공하는 에이전트입니다.
    사용자가 질문을 하면 rag_engine_tool을 사용하여 결과를 바탕으로 답변을 제공해야 합니다.
    답변을 제공할 때는 다음 형식을 엄격히 준수해야 합니다:

    1. 사용자 질문 의도 파악:
    2. 참조 문서:
    3. 답변 요약:

    참고: 항상 사용자의 질문과 동일한 언어로 답변하세요.
"""

rag_engine_tool = buid_rag_tool()

root_agent = Agent(
    name = "search_agent",
    model = os.getenv("GOOGLE_GENAI_MODEL"),
    description = "사용자 쿼리에 답변하는 에이전트",
    instruction = INSTRUCTION,
    tools=[rag_engine_tool],
)