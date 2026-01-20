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

import time
import asyncio
import argparse
from dotenv import load_dotenv

from google.genai import types
from google.adk.runners import Runner
from google.adk.events import Event, EventActions
from google.adk.sessions import InMemorySessionService

from state import agent

async def run_agent( app_name: str,
                     user_id: str, ):
    """
    ADK 이벤트 시스템을 사용하여 세션 상태를 명시적으로 수정하는 방법을 보여주는 예제입니다.

    이 함수는 초기 상태로 세션을 생성한 다음, 시스템 이벤트를 추가하여 세션 상태(예: 타임스탬프 추가)를
    업데이트하는 방법을 보여줍니다. 상태가 시간이 지남에 따라 어떻게 변하는지 보여주기 위해
    변경 전후의 세션 상태를 출력합니다.

    Args:
        app_name (str): 애플리케이션 이름.
        user_id (str): 사용자 식별자.

    Returns:
        None
    """

    session_service = InMemorySessionService()

    # 초기 상태 정의
    init_state = {
        "task_status": "아직 답변 없음",
        "timestamp": time.time(),
    }

    session = await session_service.create_session(
        app_name= app_name,
        user_id=user_id,
        state=init_state
    )
    
    print(f"\n\n1. 초기 세션 상태: {session.state}")

    runner = Runner(agent=agent.root_agent,
                    app_name=app_name,
                    session_service=session_service)

    while True:

        user_input = input("\n 👤 User: ")
        if user_input.lower().strip() in ["exit", "quit", "bye"]:
            break

        query = user_input
        content = types.Content(role='user', parts=[types.Part(text=query)])

        # 에이전트 러너를 사용하여 에이전트 이벤트를 비동기적으로 실행합니다.
        # 세션 정보는 user_id와 session_id를 통해 전달됩니다.
        events = runner.run_async(user_id=session.user_id,
                                session_id=session.id,
                                new_message=content,)

        async for event in events:
            if event.is_final_response():
                final_response = event.content.parts[0].text            
                print("\n 🤖 AI Assistant: " + final_response)

        updated_session = await session_service.get_session(app_name = session.app_name, 
                                                     user_id = session.user_id, 
                                                     session_id = session.id)

        # 업데이트된 세션 상태에서 'last_turn' 표시
        print(f"\n\n output_key - last_turn : {updated_session.state['last_turn']}")

    # 상태 변경 준비
    state_changes = {
        "task_status": f"답변 완료 : {query}",
        "timestamp": time.time(),
        "last_turn": updated_session.state['last_turn']
    }

    system_event = Event(
        invocation_id = "change-state",
        author = "system", # 또는 'agent', 'tool' 등
        actions = EventActions(state_delta=state_changes),
        timestamp = time.time()
    )

    # 상태 변경 이벤트 추가
    await session_service.append_event(session, system_event)

    print("\n\n2. 새로운 명시적 state-delta 이벤트를 추가했습니다.")

    updated_session = await session_service.get_session(app_name=session.app_name,
                                                user_id=session.user_id, 
                                                session_id=session.id)
    
    print(f"\n\n3. 이벤트를 보낸 후 세션 상태: {updated_session.state}")

if __name__ == "__main__":

    load_dotenv()

    print("에이전트 실행 중...")
    print("사용법 : uv run -m state.runner --app_name <app_name> --user_id <user_id> ")

    parser = argparse.ArgumentParser(description="사용자 쿼리로 ADK 에이전트를 실행합니다.")
    parser.add_argument("--app_name",type=str,help="이 에이전트의 애플리케이션 이름입니다.",)
    parser.add_argument("--user_id",type=str,help="이 에이전트와 상호 작용하는 사용자입니다.",)
    args = parser.parse_args()
    
    asyncio.run(run_agent(app_name = args.app_name, 
                          user_id = args.user_id,))
