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

from typing import AsyncGenerator
from typing_extensions import override

from google.adk.agents import LlmAgent, BaseAgent, SequentialAgent
from google.adk.agents.invocation_context import InvocationContext

from google.adk.events import Event
from google.adk.agents import SequentialAgent

class CriticAgent(BaseAgent):
    """
    하위 에이전트를 사용하여 다단계 비평 워크플로를 조정합니다.

    CriticAgent는 세 가지 LlmAgent 하위 에이전트인 positive_critic_agent,
    negative_critic_agent 및 review_critic_agent를 조정합니다. 긍정적 비평,
    부정적 비평, 마지막으로 리뷰 비평을 실행하여 각 단계에서 생성된 이벤트를 생성합니다.
    필요한 출력 조건이 충족되지 않는 경우(예: 상태에서 특정 키워드가 누락된 경우)
    에이전트는 워크플로를 조기에 중단할 수 있습니다. 이를 통해 사용자 입력 또는
    생성된 콘텐츠에 대한 조건부 다단계 평가 및 검토가 가능합니다.

    Attributes:
        positive_critic_agent (LlmAgent): 긍정적인 비판을 생성하는 에이전트.
        negative_critic_agent (LlmAgent): 부정적인 비판을 생성하는 에이전트.
        review_critic_agent (LlmAgent): 집계된 비평을 검토하는 에이전트.
        sequential_agent (SequentialAgent): 워크플로를 관리하는 데 사용되는 내부 순차 에이전트.

    Methods:
        _run_async_impl(ctx): 비평 워크플로를 비동기적으로 실행하고 이벤트를 생성합니다.
    """

    positive_critic_agent: LlmAgent
    negative_critic_agent: LlmAgent
    review_critic_agent: LlmAgent

    sequential_agent: SequentialAgent

    # model_config allows setting Pydantic configurations if needed, e.g., arbitrary_types_allowed
    model_config = {"arbitrary_types_allowed": True}

    def __init__(
        self,
        name: str,
        positive_critic_agent: LlmAgent,
        negative_critic_agent: LlmAgent,
        review_critic_agent: LlmAgent,
    ):
        sequential_agent = SequentialAgent(
            name="PostProcessing", sub_agents=[positive_critic_agent, negative_critic_agent]
        )

        sub_agents_list = [
            sequential_agent,
            review_critic_agent,
        ]

        super().__init__(
            name=name,
            positive_critic_agent=positive_critic_agent,
            negative_critic_agent=negative_critic_agent,
            review_critic_agent=review_critic_agent,
            sequential_agent=sequential_agent,
            sub_agents=sub_agents_list,
        )

    @override
    async def _run_async_impl(self, ctx: InvocationContext) -> AsyncGenerator[Event, None]:

        """
        다단계 비평 워크플로를 비동기적으로 실행합니다.

        이 메서드는 긍정적, 부정적 및 검토 비평 에이전트를 순서대로 실행하여
        각 단계에서 이벤트를 생성합니다. 필요한 출력 조건이 충족되지 않는 경우
        (예: 단계 후 상태에 누락된 키워드), 워크플로가 조기에 중단될 수 있습니다.
        이는 사용자 입력 또는 생성된 콘텐츠에 대한 조건부 단계적 평가 및 검토를 지원합니다.

        Args:
            ctx (InvocationContext): 세션 및 상태를 포함하는 호출 컨텍스트.

        Yields:
            Event: 워크플로 실행 중에 하위 에이전트가 생성한 이벤트.
        """

        #-----------[positive_critic_agent]--------------
        print(f"[{self.name}] Running positive_critic_agent...")
        async for event in self.positive_critic_agent.run_async(ctx):

            print(f"[{self.name}] positive_critic_agent의 이벤트: {event.model_dump_json(indent=2, exclude_none=True)}")
            yield event  # 이벤트를 yield하고 다음 단계로 이동

        # 긍정적 비평 결과에 대한 선택적 조기 종료 확인:
        # 긍정적 비평 출력을 검사하고 필요한 키워드가 누락된 경우 워크플로를 중단합니다.
        # 아래 예제는 주석 처리되어 있지만 조건부 중지 로직을 구현하는 방법을 보여줍니다.
        # if "images" not in ctx.session.state["positive_critic_output"].lower():
        #     print(f"[{self.name}] Failed to generate answer since no mention about images. Aborting workflow.")
        #     return  # Stop processing if positive critic failed

        #-----------[negative_critic_agent]--------------
        print(f"[{self.name}] Running negative_critic_agent...")
        async for event in self.negative_critic_agent.run_async(ctx):
            print(f"[{self.name}] negative_critic_agent의 이벤트: {event.model_dump_json(indent=2, exclude_none=True)}")
            yield event  # 이벤트를 yield하고 다음 단계로 이동

        # 부정적 비평 결과에 대한 선택적 조기 종료 확인:
        # 특정 조건이 충족되지 않으면(예: 키워드 누락) 워크플로를 중단합니다.
        # 예제 (주석 처리됨):
        # if "social" not in ctx.session.state["negative_critic_output"].lower():
        #     print(f"[{self.name}] Failed to generate answer since no mention about social issues. Aborting workflow.")
        #     return  # Stop processing if negative critic failed

        #-----------[review_critic_agent]--------------
        print(f"[{self.name}] Running review_critic_agent")
        async for event in self.review_critic_agent.run_async(ctx):
            print(f"[{self.name}] Event from review_critic_agent: {event.model_dump_json(indent=2, exclude_none=True)}")
            yield event
