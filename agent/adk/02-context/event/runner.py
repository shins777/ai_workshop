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

from google.genai import types
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner

from event import agent

async def run_agent():
    """
    이 예제는 ADK에서의 이벤트 기반 처리를 보여줍니다.
    사용자 쿼리로 AI 에이전트를 비동기적으로 실행합니다.

    이 함수는 사용자 세션을 생성하고, 에이전트 러너를 초기화하며,
    에이전트에게 사용자 쿼리를 전송하고, 에이전트 이벤트를 스트리밍하고,
    각 단계에 대한 상세 이벤트 정보를 출력하며, 최종 응답을 콘솔에 표시합니다.

    인자:
        없음

    반환값:
        없음
    """

    APP_NAME = "AI_assistant"
    USER_ID = "Forusone"

    # 세션 서비스를 생성하고 초기화합니다.
    # 세션 서비스는 메모리에서 세션을 관리합니다.
    # InMemorySessionService는 ADK에서 제공하는 기본 세션 서비스입니다.
    session_service = InMemorySessionService()
    session = await session_service.create_session(app_name=APP_NAME,
                                            user_id=USER_ID,
                                            state={"initial_key": "initial_value"})
    # 에이전트 러너를 생성합니다.
    # 러너는 에이전트를 세션 서비스와 연결하여 사용자 입력을 처리합니다.
    runner = Runner(agent=agent.root_agent,
                    app_name=session.app_name,
                    session_service=session_service)
    
    # 지속적으로 사용자 입력을 읽고 처리합니다.
    # 루프를 종료하려면 "exit" 또는 "quit"을 입력하세요.
    while True:

        query = input("\n 👤 User: ")
        if query.strip().lower() in ["exit", "quit"]:
            break
        
        # 사용자 입력으로부터 Content 객체를 생성합니다.
        content = types.Content(role='user', parts=[types.Part(text=query)])

        # 러너를 사용하여 에이전트 이벤트를 비동기적으로 실행합니다.
        events = runner.run_async(user_id=session.user_id,
                                session_id=session.id,
                                new_message=content,
                                )
        # 이벤트 스트림을 비동기적으로 처리합니다.
        async for event in events:
            print("\n\n-------------------------")
            print(f"event.invocation_id: {event.invocation_id}")
            print(f"event.author: {event.author}")
            print(f"event.actions: {event.actions}")
            print(f"event.branch: {event.branch}")    
            print(f"event.id: {event.id}")
            print(f"event.is_final_response(): {event.is_final_response()}")        
            
            # 이벤트에 근거(grounding) 콘텐츠(참조 데이터)가 포함되어 있으면 출력합니다.
            if event.grounding_metadata is not None:
                print("\n\n-----------< Grounding service information >--------------")

                if event.grounding_metadata.grounding_chunks is not None:
                    for grounding_chunk in event.grounding_metadata.grounding_chunks:
                        print(f"\n\n--------[ Title: {grounding_chunk.web.title} ]----------")
                        print(f"* grounding_chunk.web.domain: {grounding_chunk.web.domain}")
                        print(f"* grounding_chunk.web.url: {grounding_chunk.web.uri}")
                    
            if event.is_final_response():
                final_response = event.content.parts[0].text            
                print(f"\n 🤖 AI Assistant: {final_response}\n")

if __name__ == "__main__":
    import asyncio
    import argparse

    print("Running the agent...")
    print(""" Usage : uv run -m event.runner """)
    parser = argparse.ArgumentParser(description="Run the ADK agent with a user query.")
    args = parser.parse_args()
    asyncio.run(run_agent())