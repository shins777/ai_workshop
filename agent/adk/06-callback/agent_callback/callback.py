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
from typing import Optional
from google.adk.agents.callback_context import CallbackContext

#----------------------------------[ callback_before_agent ]------------------------------------

def callback_before_agent(callback_context: CallbackContext) -> Optional[types.Content]:

    """
    에이전트 실행 전에 호출되는 전처리 콜백입니다.

    이 함수는 CallbackContext에서 현재 상태를 검사합니다. 상태의
    'skip_agent' 플래그가 True로 설정된 경우 에이전트 실행을 중단하고 사용자에게
    맞춤 응답을 반환합니다. 그렇지 않으면 None을 반환하여 에이전트가 정상적으로 실행되도록 합니다.

    Args:
        callback_context (CallbackContext): 에이전트 정보 및 상태를 포함하는 컨텍스트
    Returns:
        Optional[types.Content]: 에이전트를 건너뛸 때의 사용자 정의 Content 응답 또는 계속하려면 None.
    """

    # CallbackContext에서 컨텍스트 정보를 검색합니다.
    agent_name = callback_context.agent_name
    current_state = callback_context.state.to_dict()

    # 상태 정보에 따라 실행 전 흐름을 제어합니다.
    if current_state.get("skip_agent", False):
        print(f"[Before Agent] 조건 충족: 상태 플래그로 인해 에이전트 실행 건너뜀 - Agent: {agent_name} : Current State: {current_state}")

        # 에이전트를 호출하지 않고 사용자에게 반환할 Content 응답을 생성합니다.
        return_content = types.Content(
            parts=[types.Part(text=f"사용자 상태 플래그로 인해 before_agent_callback에서 에이전트 {agent_name} 실행을 건너뛰었습니다.")],
            role="model"  # 응답의 역할을 'model'로 설정
        )
        return return_content
    else:  # None을 반환하여 에이전트가 정상적으로 실행되도록 합니다.
        print(f"[Before Agent] 에이전트 실행 중 - {agent_name} 진행 중.")
        return None  # None을 반환하면 LlmAgent가 정상적으로 실행됩니다.



#----------------------------------[ callback_after_agent ]------------------------------------

def callback_after_agent(callback_context: CallbackContext) -> Optional[types.Content]:
    """
    에이전트 실행 후 호출되는 후처리 콜백입니다.

    이 함수는 CallbackContext에서 현재 상태를 검사합니다. 상태의
    'check_response' 플래그가 설정된 경우 사용자에게 맞춤 응답을 반환하고
    추가 처리를 중단합니다. 그렇지 않으면 None을 반환하여 정상적인 사후 에이전트 흐름을 계속합니다.

    Args:
        callback_context (CallbackContext): 에이전트 정보 및 상태를 포함하는 컨텍스트
    Returns:
        Optional[types.Content]: 후처리를 위한 사용자 정의 Content 응답 또는 계속하려면 None.
    """
    
    # CallbackContext에서 컨텍스트 정보를 검색합니다.
    agent_name = callback_context.agent_name
    current_state = callback_context.state.to_dict()

    print(f"[After Agent] current_state : Current State: {current_state}")

    # 상태 정보에 따라 실행 후 흐름을 제어합니다.
    if current_state.get("check_response"):
        print(f"[After Agent] 조건 충족: 사후 에이전트 응답 처리 - {agent_name} : Current State: {current_state}")

        print(f"## Callback context info : {callback_context}")
        # 에이전트 호출 후 추가 처리를 중단하고 사용자를 위한 알림 Content를 생성합니다.
        return types.Content(
            parts=[types.Part(text=f"상태 플래그로 인해 에이전트 호출 후 에이전트 {agent_name}의 콜백이 실행되었습니다.")],
            role="model"  # 응답의 역할을 'model'로 설정
        )
    
    else:
        print(f"[After Agent] 조건 미충족: 에이전트 {agent_name} 계속 진행.")
        return None  # None을 반환하면 LlmAgent가 정상적으로 계속됩니다.