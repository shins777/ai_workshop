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
from google.adk.tools import VertexAiSearchTool
import vertexai

load_dotenv(dotenv_path="../../.env")

def get_vertex_search_tool():
    """
    Vertex AI Search 도구 인스턴스를 생성하고 구성합니다.
    이 함수는 프로젝트, 위치, 프로젝트 번호 및 데이터 스토어 ID에 필요한 환경 변수를 로드하고,
    Vertex AI 환경을 초기화하고, 데이터 스토어 리소스 경로를 구성하고,
    지정된 데이터 스토어에 연결된 VertexAiSearchTool 인스턴스를 반환합니다.

    Returns:
        VertexAiSearchTool: 지정된 Vertex AI Search 데이터 스토어에 연결된 인스턴스입니다.
    """

    # Vertex AI Search is available in the global location, so set VERTEXAI_LOCATION to "global".
    # When constructing data_store_id, use the project number and datastore ID to build the full path.
    VAIS_PROJECT_NUMBER = os.getenv('VAIS_PROJECT_NUMBER')
    VAIS_LOCATION = os.getenv('VAIS_LOCATION')  # Vertex AI Search는 글로벌 위치에서 사용 가능
    VAIS_DATASTORE_ID = os.getenv('VAIS_DATASTORE_ID')

    data_store_id = f"projects/{VAIS_PROJECT_NUMBER}/locations/{VAIS_LOCATION}/collections/default_collection/dataStores/{VAIS_DATASTORE_ID}"
    print("Vertex AI Search : Data store ID : \n", data_store_id)

    vertex_search_tool = VertexAiSearchTool(data_store_id=data_store_id)
    print("Vertex AI Search : vertex_search_tool : \n", vertex_search_tool)

    return vertex_search_tool

 
INSTRUCTION = """
    당신은 사용자 질문에 답변을 제공하는 에이전트입니다.
    사용자가 질문을 하면 'vertex_search_tool'을 사용하여 검색을 수행하고 결과를 바탕으로 답변을 제공해야 합니다.
"""

vertex_search_tool = get_vertex_search_tool()
print("Vertex AI Search : vertex_search_tool : \n", vertex_search_tool)

root_agent = Agent(
    name = "vertexai_search",
    model = os.getenv("GOOGLE_GENAI_MODEL"),
    description = "사용자 쿼리에 답변하는 에이전트",
    instruction = INSTRUCTION,
    tools=[vertex_search_tool],
)