import requests
from datetime import datetime, timedelta
#import 로 datetime 과 timedelta 라이브러리 블러옴
def get_aws_data():
    #변수 파라미터 지정
    AUTH_KEY = "blE3_YUlTT2RN_2FJZ091Q"
    STN_ID = "133"
    url = "https://apihub.kma.go.kr/api/typ01/cgi-bin/url/nph-aws2_min?tm2=202302010900&stn=0&disp=0&help=1&authKey=blE3_YUlTT2RN_2FJZ091Q"


now = datetime.now()
request_time = now - timedelta(minutes=3)
#현재시간에서 3분뺀 라이브 정보
target_time = request_time.strftime("%Y%m%d%H%M")

params = {
    'tm2': target_time,
    'stn': station_id,
    'disp': '1',
    'help': '0',
    'authKey': auth_key
} 
#requests 라이브러리 params 를 사용해 파라미터 지정

print(f"[요청 시각] 현재 시간: {now.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"[API 요청] 조회 대상 시각 (3분 전): {target_time}\n")

try:
    response = request_get(url, params=params)

    if response.stastus_code == 200:
        raw_text = response.text
        lines = raw_text.strip().split('\n')

        for line in lines:
            