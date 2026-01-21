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
import argparse

import vertexai
from vertexai import agent_engines
#from vertexai.preview.reasoning_engines import AdkApp
from vertexai.agent_engines import AdkApp

from .agent import root_agent

load_dotenv()

if __name__ == "__main__":
    
    print(""" 사용법 : uv run -m agent_engine.deploy --agent_name 'adk_agent_20250730'""")
    parser = argparse.ArgumentParser(description="사용자 쿼리로 ADK 에이전트를 실행합니다.")
    parser.add_argument("--agent_name",type=str,help="에이전트 이름.",)

    args = parser.parse_args()
    agent_name = args.agent_name

    env_vars = {
        "GOOGLE_CLOUD_AGENT_ENGINE_ENABLE_TELEMETRY": "true",
        "OTEL_INSTRUMENTATION_GENAI_CAPTURE_MESSAGE_CONTENT": "true",
    }

    # Vertex AI 환경 초기화 : Agent Engine을 배포하기 위한 환경 설정
    # Agent Engine 과 Gemini 모델을 사용하기 위한 리전을 다르게 할 수 있음.
    vertexai.init(
        project=os.getenv("GOOGLE_CLOUD_PROJECT"),
        location=os.getenv("AGENT_ENGINE_LOCATION"),
        staging_bucket=os.getenv("AGENT_ENGINE_BUCKET"),
    )

    # adk_app 생성
    adk_app = AdkApp(agent=root_agent)

    # Agent Engine 환경 설정
    display_name = agent_name
    gcs_dir_name = os.getenv("AGENT_ENGINE_BUCKET")
    description = "사용자 질문에 대한 AI 정보 검색 어시스턴트"
    requirements = [
        "google-adk[vertexai]",
        "google-cloud-aiplatform[adk,agent-engines]",
        "cloudpickle==3.0",
        "python-dotenv",
    ]

    remote_agent = agent_engines.create(
                    adk_app,
                    display_name=display_name,
                    gcs_dir_name = gcs_dir_name,
                    description=description,
                    requirements=requirements,
                    extra_packages = []
    )