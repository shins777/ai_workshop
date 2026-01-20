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

from google.adk.sessions import InMemorySessionService
from google.adk.sessions import DatabaseSessionService
from google.adk.sessions import VertexAiSessionService

import asyncio
from google.genai import types
from google.adk.sessions import BaseSessionService
from google.adk.runners import Runner

from session import agent

#--------------------------------[run_agent]----------------------------------

async def run_agent(
    session_service: BaseSessionService,
    app_name: str,
    user_id: str,
    session_id: str = None,
):
    """
    세션 인식 대화형 루프에서 에이전트를 실행합니다.

    이 함수는 사용자와 애플리케이션에 대한 기존 세션이 있는지 확인합니다.
    세션이 존재하면 가장 최근 세션을 계속하고, 그렇지 않으면 새 세션을 생성합니다.
    그런 다음 사용자 입력을 읽고, 입력을 에이전트에게 전달하고, 에이전트 응답을 출력하는 루프에 진입합니다.
    각 상호작용 후에는 세션 상태와 이벤트를 출력합니다.

    Args:
        session_service (BaseSessionService): 사용자 세션을 관리하는 세션 서비스.
        app_name (str): 애플리케이션 이름.
        user_id (str): 사용자 식별자.
        session_id (str): 세션 식별자.

    Returns:
        None
    """

    # 주어진 app_name 및 user_id에 대해 세션 서비스에서 기존 세션을 쿼리합니다.
    existing_sessions = await session_service.list_sessions(
        app_name=app_name,
        user_id=user_id,
    )
    
    # 주어진 session_id를 가진 세션이 존재하는지 확인합니다. session_id가 None이면 결과는 None이 됩니다.
    existing_session_id = next((session_id for session in existing_sessions.sessions if session.id == session_id), None)
    
    if existing_session_id is None:
        # 기존 세션이 없으면 새 세션을 생성합니다.
        
        if isinstance(session_service, VertexAiSessionService): 
            # VertexAiSessionService를 사용하는 경우 create_session에 session_id를 전달하지 마세요. (2025년 8월 기준 google-adk==1.12.0)        
            new_session = await session_service.create_session(
                app_name=app_name,
                user_id=user_id,
                state=None)        
            
        else:
            # 다른 세션 서비스의 경우 session_id를 create_session에 전달하여 특정 세션 ID를 설정할 수 있습니다.
            new_session = await session_service.create_session(
                app_name=app_name,
                user_id=user_id,
                state=None,
                session_id=session_id, )
        
        new_session_id = new_session.id
        print(f"새 세션 생성됨: {new_session_id}")

    else:
        print(f"기존 세션 사용: {existing_session_id}")

    session_id = existing_session_id or new_session_id

    # 에이전트 러너 초기화.
    runner = Runner(agent=agent.root_agent,
                    app_name=app_name,
                    session_service=session_service)

    while True:

        query = input("\n 👤 User: ")
        if query.strip().lower() in ["exit", "quit"]:
            break

        content = types.Content(role='user', parts=[types.Part(text=query)])

        # 에이전트 러너를 사용하여 에이전트 이벤트를 비동기적으로 실행합니다.
        # 세션을 유지하기 위해 user_id와 session_id를 제공합니다. 대화당 하나의 세션만 사용됩니다.
        # 새 세션 생성을 강제하려면 session_id=None을 전달하세요.
        events = runner.run_async(user_id=user_id,
                                session_id=session_id,
                                new_message=content, )

        async for event in events:
            await asyncio.create_task(print_session(app_name = app_name,
                                                    user_id = user_id,
                                                    session_id = session_id,
                                                    session_service = session_service))
            if event.is_final_response():
                final_response = event.content.parts[0].text            
                print("\n 🤖 AI Assistant: " + final_response)

#--------------------------------[print_session]----------------------------------

async def print_session(app_name: str,
                        user_id: str,
                        session_id: str,
                        session_service: BaseSessionService):
    """
    세션 속성을 검색하고 출력합니다.

    이 함수는 제공된 애플리케이션 이름, 사용자 ID 및 세션 ID를 사용하여 세션 서비스에서 세션 객체를 가져옵니다.
    그런 다음 주요 세션 속성(id, app_name, user_id, state, events, 마지막 업데이트 시간)을 출력합니다.

    Args:
        app_name (str): 애플리케이션 이름.
        user_id (str): 사용자 ID.
        session_id (str): 세션 ID.
        session_service (BaseSessionService): 세션 서비스 인스턴스.

    Returns:
        None
    """

    # app_name, user_id, session_id를 사용하여 세션 서비스에서 세션을 가져옵니다.
    session  = await session_service.get_session(app_name=app_name,
                                user_id=user_id,
                                session_id=session_id,)

    print(f"--- 세션 속성 검사 ---")
    print(f"ID (`id`):                {session.id}")
    print(f"애플리케이션 이름 (`app_name`): {session.app_name}")
    print(f"사용자 ID (`user_id`):         {session.user_id}")
    print(f"상태 (`state`):           {session.state}") # 참고: 여기서는 초기 상태만 표시됩니다.
    # print(f"Events (`events`):         {session.events}") # 초기에는 비어 있음
    print(f"마지막 업데이트 (`last_update_time`): {session.last_update_time:.2f}")
    print(f"---------------------------------")

#--------------------------------[Main entry point function ]----------------------------------

if __name__ == "__main__":
    import asyncio
    import argparse

    """이 스크립트는 ADK 에이전트를 실행하는 주요 진입점입니다.
    제공된 세션 유형에 따라 적절한 세션 서비스를 선택하고
    대화형 에이전트 루프를 시작합니다.

    Args:
        --type (str): 세션 유형. 'in_memory', 'database', 'agent_engine' 중 하나를 선택하세요.
        --app_name (str): 에이전트가 사용하는 애플리케이션 이름입니다.
        --user_id (str): 에이전트와 상호 작용하는 사용자 식별자입니다.
        --session_id (str): 에이전트와 상호 작용하는 세션 식별자입니다.

    Raises:
        ValueError: 잘못된 세션 유형이 제공된 경우.
    """

    load_dotenv()

    print("에이전트 실행 중...")
    print("사용법 : uv run -m session.runner --type [in_memory|database|agent_engine] --app_name <app_name> --user_id <user_id> --session_id <session_id>")

    parser = argparse.ArgumentParser(description="사용자 쿼리로 ADK 에이전트를 실행합니다.")
    parser.add_argument("--type",type=str,help="세션 유형",)
    parser.add_argument("--app_name",type=str,help="이 에이전트의 애플리케이션 이름입니다.",)
    parser.add_argument("--user_id",type=str,help="이 에이전트와 상호 작용하는 사용자 이름입니다.",)
    parser.add_argument("--session_id",type=str,help="이 에이전트와 상호 작용하는 세션 ID입니다.",)

    args = parser.parse_args()

    session_service = None
    agent_engine_resource_name = None

    if args.type == "in_memory":
        session_service = InMemorySessionService()
    
    elif args.type == "database":
        db_url = "sqlite:///./adk_session.db"
        session_service = DatabaseSessionService(db_url=db_url)
    
    elif args.type == "agent_engine":
        PROJECT_ID = os.environ['GOOGLE_CLOUD_PROJECT']
        AGENT_LOCATION = os.environ['GOOGLE_CLOUD_LOCATION']
        AGENT_ENGINE_ID = os.environ['AGENT_ENGINE_ID']

        session_service = VertexAiSessionService(project=PROJECT_ID, 
                                                 location=AGENT_LOCATION,
                                                 agent_engine_id = AGENT_ENGINE_ID)
    else:
        raise ValueError("잘못된 세션 유형입니다. 'in_memory', 'database', 'agent_engine' 중 하나를 선택하세요.")

    asyncio.run(run_agent(session_service = session_service, 
                                 app_name = args.app_name, 
                                 user_id = args.user_id, 
                                 session_id = args.session_id ) )
