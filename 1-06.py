# datetime 모듈

# 1-06.py

from datetime import datetime, timezone, timedelta

now = datetime.now() # 현재 날짜/시각 정보를 가진 datetime 객체를 얻음
print("{0}-{1:02}-{2:02} {3:02}:{4:02}:{5:02}".format(now.year,now.month,now.day,now.hour,now.minute,now.second))

fmt = "%Y{0} %m{1} %d{2} %H{3} %M{4} %S{5}" 
print(now.strftime(fmt).format(*"년월일시분초")) # strftime() : 날짜 형식 변경