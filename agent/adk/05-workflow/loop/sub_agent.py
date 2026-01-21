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

import os
from dotenv import load_dotenv

from google.adk.agents import Agent
from google.adk.tools import ToolContext
from google.adk.tools import google_search

load_dotenv()

COMPLETION_PHRASE = "Overall, the answer is fine."

#--------------------------------[exit_loop]----------------------------------

def exit_loop(tool_context: ToolContext):
    """
    루프 에이전트에게 현재 반복을 종료하도록 신호를 보냅니다.

    이 함수는 루프 에이전트 내에서 도구로 호출되도록 의도되었습니다.
    제공된 ToolContext에 `escalate` 작업 플래그를 설정하여 루프 컨트롤러에게
    워크플로의 다음 단계로 진행하도록 신호를 보냅니다.

    Args:
        tool_context (ToolContext): 에이전트 및 작업 정보를 포함하는 컨텍스트 객체.

    Returns:
        dict: 추가 출력이 필요하지 않으므로 빈 딕셔너리입니다.
    """
  
    print(f"[Tool Call] exit_loop triggered by {tool_context.agent_name}")
    
    # 루프 에이전트에게 현재 반복을 종료하도록 신호를 보냅니다.
    # 도구 컨텍스트에 'escalate' 작업 플래그를 설정하여 루프 컨트롤러가
    # 루프를 빠져나와 다음 워크플로 단계로 계속 진행할 수 있도록 합니다.
    tool_context.actions.escalate = True

    return {}

#--------------------------------[research_agent]----------------------------------

# research_agent: 주제에 대한 초기 콘텐츠를 수집하거나 생성합니다.
research_agent = Agent(
    name = "research_agent",
    model = os.getenv("GOOGLE_GENAI_MODEL"),
    description = "주어진 주제에 대해 긍정적인 측면과 부정적인 측면을 작성하는 에이전트입니다.",
    instruction = """
            당신은 주어진 주제에 대한 긍정적인 측면과 부정적인 측면을 작성하는 에이전트입니다.
            응답을 제공할 때 각 측면에 대해 3줄로 간결하고 명확하게 답변해야 하며 "### Research Results: "로 시작해야 합니다.
            """,
    tools=[google_search],
    output_key="research_outcome",
)

#--------------------------------[critic_agent]----------------------------------

# critic_agent: 연구 결과에 대해 간결하고 건설적인 비평을 생성합니다.
critic_agent = Agent(
    name = "critic_agent",
    model = os.getenv("GOOGLE_GENAI_MODEL"),
    description = "주어진 주제에 대한 답변을 검토하는 건설적인 비평 AI 에이전트입니다.",
    instruction = f"""
                    당신은 주어진 주제에 대해 제공된 답변을 검토하는 건설적인 비평 AI 에이전트입니다.
                    응답에 "### 답변 검토"라는 제목을 추가하세요.

                    **주제에 대해 제공된 답변:**
                        ```
                        {{research_outcome}}
                        ```
                    **작업:**
                        다음 기준에 따라 답변을 명확하게 검토하세요:
                        - 필요한 경우 웹 검색 도구(도구: google_search)를 사용하여 추가 정보를 수집할 수 있습니다.
                        - 응답을 개선할 수 있는 *명확하고 실행 가능한* 방법 1-2가지를 제안하세요.
                        - 관련된 경우 사회 및 조직에 대한 시사점을 포함하세요.
                        - 간결하고 구체적인 제안을 제공하세요. 예: 비평 텍스트*만* 출력합니다.
                    **답변이 허용 가능한 경우:**
                        정확히 "{COMPLETION_PHRASE}"라는 문구로 응답하고 다른 텍스트나 설명은 출력하지 마세요.

                """,
    tools=[google_search],
    output_key="criticism",
)

#--------------------------------[refine_agent]----------------------------------

# refine_agent: 비평 제안을 적용하거나 비평이 결과가 만족스럽다고 표시할 때
# `exit_loop`를 호출합니다.
refine_agent = Agent(
    name = "refine_agent",
    model = os.getenv("GOOGLE_GENAI_MODEL"),
    description = "비평을 평가하고 적용하여 답변을 개선하는 건설적인 개선 에이전트입니다.",
    instruction = f"""
                    당신은 사용자의 답변을 검토하는 건설적인 개선 에이전트입니다.
                    응답에 "## 답변 검증"이라는 제목을 추가하세요.

                    **주제에 대해 제공된 답변:**
                        ```
                        {{research_outcome}}
                        ```
                    **비평 / 제안:**
                        ```
                        {{criticism}}
                        ```
                    **작업:**
                        '비평 / 제안'을 분석하세요.

                        비평이 정확히 "{COMPLETION_PHRASE}"인 경우:
                            'exit_loop' 함수를 호출하세요. 텍스트를 출력하지 마세요.
                        그렇지 않으면 (비평에 실행 가능한 피드백이 포함된 경우):
                            제안 사항을 신중하게 적용하여 '현재 문서'를 개선하세요. 개선된 문서 텍스트*만* 출력하세요.
                            설명을 추가하지 마세요. 개선된 문서를 출력하거나 exit_loop 함수를 호출하세요.
                """,
    
    tools=[exit_loop],

)

#--------------------------------[conclusion_agent]----------------------------------
# conclusion_agent: 긍정적 측면과 부정적 측면을 요약하고 최종 요약을 생성합니다.
conclusion_agent = Agent(
    name = "conclusion_agent",
    model = os.getenv("GOOGLE_GENAI_MODEL"),
    description = "사용자 검색어의 긍정적 측면과 부정적 측면을 요약하고 최종 요약을 제공하는 에이전트입니다.",
    instruction = f"""
                    당신은 주어진 주제에 대한 긍정적 및 부정적 비평을 바탕으로 최종 요약 및 결론을 설명하는 에이전트입니다.
                    응답할 때 현재 문서와 아래의 비평/제안 섹션을 참조하고 답변을 "### 최종 요약"으로 시작하세요.
                    
                    **주제에 대해 제공된 답변:**
                    ```
                    {{research_outcome}}
                    ```
                    **비평 / 제안:**
                    ```
                    {{criticism}}
                    ```

                    응답을 제공할 때 가능한 한 간결하고 명확하게 3줄로 작성해야 합니다.   

                """,
)