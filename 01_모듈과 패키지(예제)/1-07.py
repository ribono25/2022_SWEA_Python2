# pytz 서드파티 모듈 사용법

# 1-07.py

from datetime import datetime
from pytz import common_timezones, timezone, utc

# pip install 모듈명 : 서드파티 모듈 설치
# pip uninstall 모듈명 : 서드파티 모듈 삭제

for tz in list(common_timezones): # common_timezones : 타임존 정보 가짐
    if tz.lower().find("paris") >= 0: # find : 문자열 존재 시 인덱스 반환, 미존재 시 -1 반환
        print(tz)

tz_utc = timezone(utc.zone)
tz_seoul = timezone("Asia/Seoul")
tz_pacific = timezone("US/Pacific")
tz_paris = timezone("Europe/Paris")

fmt = "%Y-%m-%d %H:%M:%S %Z%z" # %Z : 타임존 명칭, %z : UTC 기준시각과의 차이

now_utc = datetime.now(tz_utc)
print(now_utc.strftime(fmt))
now_seoul = datetime.now(tz_seoul)
print(now_seoul.strftime(fmt))
now_pacific = datetime.now(tz_pacific)
print(now_pacific.strftime(fmt))
now_paris = datetime.now(tz_paris)
print(now_paris.strftime(fmt))