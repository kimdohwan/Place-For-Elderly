import json

import requests
from requests.adapters import HTTPAdapter
from urllib3 import Retry

from config import settings

# - 기본 파라미터
#     'KEY': 발급받은 api key,
#     'Type': json 또는 xml
#     'pindex': 페이지 인덱스
#     'pSize': 최대 1000개까지 요청 가능
# - 요청 가능 파라미터
#     'SIGUN_CD': 시/군 코드
#     'SIGUN_NM': 시/군 한글명
# - 응답 코드 종류
#     구분	코드	설명
#     ERROR	300	필수 값이 누락되어 있습니다. 요청인자를 참고 하십시오.
#     ERROR	290	인증키가 유효하지 않습니다. 인증키가 없는 경우, 홈페이지에서 인증키를 신청하십시오.
#     ERROR	336	데이터요청은 한번에 최대 1,000건을 넘을 수 없습니다.
#     ERROR	333	요청위치 값의 타입이 유효하지 않습니다.요청위치 값은 정수를 입력하세요.
#     ERROR	310	해당하는 서비스를 찾을 수 없습니다. 요청인자 중 SERVICE를 확인하십시오.
#     ERROR	337	일별 트래픽 제한을 넘은 호출입니다. 오늘은 더이상 호출할 수 없습니다.
#     ERROR	500	서버 오류입니다. 지속적으로 발생시 홈페이지로 문의(Q&A) 바랍니다.
#     ERROR	600	데이터베이스 연결 오류입니다. 지속적으로 발생시 홈페이지로 문의(Q&A) 바랍니다.
#     ERROR	601	SQL 문장 오류 입니다. 지속적으로 발생시 홈페이지로 문의(Q&A) 바랍니다.
#     INFO	000	정상 처리되었습니다.
#     INFO	300	관리자에 의해 인증키 사용이 제한되었습니다.
#     INFO	200	해당하는 데이터가 없습니다.

BASE_URL = 'https://openapi.gg.go.kr'
API_NAME = 'OldPersonRecuperationFacility'
API_KEY = settings.secrets['API_KEY']
SUCCESS_CODE = ['INFO-000', 'INFO-200']


def get_api_data():
    url = BASE_URL + '/' + API_NAME
    api_data = []

    # pindex 1 부터 데이터가 없을 때까지 while loop 진행
    pindex = 1
    while True:
        payload = {
            'KEY': API_KEY,
            'Type': 'json',
            'pindex': pindex
        }

        # ConnectionError 발생 시 requests session 설정을 바꿔 진행
        try:
            res = requests.get(url, params=payload)
        except requests.ConnectionError:
            session = requests.Session()
            retry = Retry(connect=3, backoff_factor=0.5)
            adapter = HTTPAdapter(max_retries=retry)
            session.mount('https://', adapter)
            res = session.get(url, params=payload)

        j = json.loads(res.text)

        # 더 이상 불러올 데이터가 없거나(INFO-200), 잘못된 요청일 경우 while loop 중단
        if API_NAME not in j.keys():
            code = j['RESULT']['CODE']
            message = j['RESULT']['MESSAGE']

            # 데이터를 모두 불러온 경우 return
            if code in SUCCESS_CODE:
                return api_data

            # 중단된 이유를 나타내는 code 와 message 출력 후 중단
            print(code, message)
            break

        # 시설 리스트를 json(j) 에서 얻은 후, 날짜 포멧을 변경하는 함수 실행
        facility_list = j[API_NAME][1]['row']
        facility_list = change_date_format(facility_list)

        # return 될 api_data 에 시설 리스트를 추가
        api_data += facility_list

        pindex += 1


# 날짜를 저장 가능한 포멧으로 변경
# 20111230 과 같이 들어오는 포멧을 2011-12-30으로 변환하는 함수
def change_date_format(facility_list):
    # l_data: 인허가일자
    # c_date: 폐업일자
    for facility in facility_list:
        l_date = facility['LICENSG_DE']
        if l_date is not None:
            facility['LICENSG_DE'] = l_date[:4] + '-' + l_date[4:6] + '-' + l_date[6:]
        c_date = facility['CLSBIZ_DE']
        if c_date is not None:
            facility['CLSBIZ_DE'] = c_date[:4] + '-' + c_date[4:6] + '-' + c_date[6:]
    return facility_list
