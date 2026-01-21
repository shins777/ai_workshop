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

from google.genai import types
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner

from agent_callback import agent

#------------------------------------------------------------------------------------

async def run_agent(command: str):
    
    """
    지정된 명령과 사용자 쿼리로 AI 에이전트를 비동기적으로 실행합니다.

    이 함수는 세션 상태에 주어진 명령을 포함하여 세션을 설정하고,
    에이전트 러너를 초기화하고, 사용자 쿼리를 처리합니다. 사용자 입력을 출력하고,
    에이전트의 응답 이벤트를 스트리밍하고, 최종 응답을 출력합니다.

    Args:
        command (str): 에이전트 콜백 동작을 제어하는 명령 (예: 'skip_agent', 'check_response')

    Returns:
        None
    """

    # print(f"\n 👤 User: {user_query}\n")

    APP_NAME = "AI_assistant"
    USER_ID = "Forusone"

    session_service = InMemorySessionService()
    session = await session_service.create_session(app_name=APP_NAME,
                                            user_id=USER_ID,
                                            # 참고: 인수로 전달된 명령을 여기서 세션 상태에 포함합니다.
                                            state={command: True})  

    runner = Runner(agent=agent.root_agent,
                    app_name=session.app_name,
                    session_service=session_service)

    query = input("\n 👤 User: ")
    content = types.Content(role='user', parts=[types.Part(text=query)])

    events = runner.run_async(user_id=session.user_id,
                              session_id=session.id,
                              new_message=content,)

    async for event in events:
        if event.is_final_response():
            final_response = event.content.parts[0].text            
            print(f"\n 🤖 AI Assistant: {final_response}\n")

#------------------------------------------------------------------------------------

if __name__ == "__main__":
    import asyncio
    import argparse

    print("에이전트 실행을 시작합니다...")
    print(""" 사용법 : uv run -m agent_callback.runner --command [skip_agent|check_response]""")
 
    parser = argparse.ArgumentParser(description="명령 및 사용자 쿼리로 ADK 에이전트 실행.")
    parser.add_argument("--command",type=str,help="에이전트의 콜백을 제어하는 명령",)

    args = parser.parse_args()
    asyncio.run(run_agent(command = args.command))