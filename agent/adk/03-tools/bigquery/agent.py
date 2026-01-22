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

import asyncio
from google.adk.agents import Agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.adk.tools.bigquery import BigQueryCredentialsConfig
from google.adk.tools.bigquery import BigQueryToolset
from google.adk.tools.bigquery.config import BigQueryToolConfig
from google.adk.tools.bigquery.config import WriteMode
from google.genai import types
import google.auth

load_dotenv(dotenv_path="../../.env")

def get_bigquery_toolset() -> BigQueryToolset:
    """
    BigQuery 도구 세트를 구성하고 반환합니다.

    이 함수는 BigQuery 인증 정보를 로드하고, BigQuery 도구 세트를 초기화하며,
    BigQueryToolConfig를 사용하여 구성합니다. 이 도구 세트는 BigQuery 데이터베이스와 상호 작용하는 데 사용됩니다.

    Returns:
        BigQueryToolset: 구성된 BigQuery 도구 세트 인스턴스
    """
    # 모든 쓰기 작업을 차단하도록 도구 구성을 정의합니다.
    tool_config = BigQueryToolConfig(write_mode=WriteMode.BLOCKED)

    # 자격 증명 구성을 정의합니다. 이 예제에서는 애플리케이션 기본 자격 증명을 사용합니다.
    # https://cloud.google.com/docs/authentication/provide-credentials-adc
    application_default_credentials, _ = google.auth.default()
    credentials_config = BigQueryCredentialsConfig(
        credentials=application_default_credentials
    )

    # BigQuery 도구 세트 인스턴스화
    bigquery_toolset = BigQueryToolset(
        credentials_config=credentials_config, bigquery_tool_config=tool_config
    )
    return bigquery_toolset

# BigQuery 도구 세트를 가져옵니다. 이것은 에이전트에서 BigQuery와 상호 작용하는 데 사용됩니다.
bigquery_toolset = get_bigquery_toolset()

INSTRUCTION = """
        당신은 BigQuery 데이터 및 모델에 대한 질문에 답변하고 SQL 쿼리를 실행하는 데이터 과학 에이전트입니다.
        BigQuery 데이터베이스에서 정보를 검색하고, SQL 쿼리를 작성 및 실행하고, 다양한 사용자 질문에 답변을 제공하세요.
        """

root_agent = Agent(
    name = "search_agent",
    model = os.getenv("GOOGLE_GENAI_MODEL"),
    description = "BigQuery 데이터 및 모델에 대한 질문에 답변하고 SQL 쿼리를 실행하는 데이터 과학 에이전트입니다.",
    instruction = INSTRUCTION,
    tools=[bigquery_toolset],
)
