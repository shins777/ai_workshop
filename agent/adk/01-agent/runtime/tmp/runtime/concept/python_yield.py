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

"""
다음은 Python의 yield 문을 비유로 사용하여 AI 에이전트 내에서 하위 에이전트가 어떻게 작동하는지 설명합니다.
핵심 개념은 위임과 흐름의 재개입니다.

위임 및 중단: 메인 에이전트는 특정 작업을 하위 에이전트에게 위임하고 자신의 작업을 일시적으로 중단합니다.
작업 처리 및 결과 반환: 하위 에이전트는 위임된 작업을 수행하고 결과를 yield합니다.
재개: 메인 에이전트는 하위 에이전트가 처리를 완료한 후 다음 작업을 재개합니다.
요약하면, 이 모델은 처리를 위해 특정 작업을 하위 에이전트에게 위임함으로써 워크플로를 효율적으로 구조화합니다.
"""
import time
def count_up_to(max_number):
    number = 0
    while number < max_number:
        # 숫자를 반환하고 함수 실행을 중단합니다; 처리가 완료되면 재개합니다.
        yield number  
        print("After yield in count_up_to:", number)
        number += 1

for num in count_up_to(5):
    print(num)  # 0, 1, 2, 3, 4를 출력합니다
    time.sleep(1)  # 1초 대기합니다
    print("Yielded in loop:", num)  # 루프에서 yield됨: 0, 1, ...