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

def get_exchange_rate(
    currency_from: str = "USD",
    currency_to: str = "KRW",
    currency_date: str = "latest", )->dict:
    """
    지정된 날짜의 두 통화 간 환율을 검색합니다.
    Frankfurter API(https://api.frankfurter.app/)를 사용하여 환율 데이터를 가져옵니다.

    Args:
        currency_from: 기준 통화(3글자 통화 코드). 기본값은 "USD"(미국 달러)입니다.
        currency_to: 대상 통화(3글자 통화 코드). 기본값은 "KRW"(한국 원)입니다.
        currency_date: 환율을 조회할 날짜입니다. 기본값은 가장 최근 환율인 "latest"입니다.
            과거 환율의 경우 YYYY-MM-DD 형식으로 지정하세요.

    Returns:
        dict: 환율 정보를 포함하는 딕셔너리입니다.
            예: {"amount": 1.0, "base": "USD", "date": "2023-11-24", "rates": {"EUR": 0.95534}}
    """

    import requests
    response = requests.get(
        f"https://api.frankfurter.app/{currency_date}",
        params={"from": currency_from, "to": currency_to},
    )
    return response.json()
