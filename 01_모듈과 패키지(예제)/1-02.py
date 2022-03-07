# import ~ as ~ 문과 모듈 별칭의 사용

# 1-02.py

import math as m # math 모듈을 m이란 별칭으로 참조 가능
# import 모듈명 as 별칭

print("m.radians(90) = {0}".format(m.radians(90)))
print("m.ceil(3.2) = {0}".format(m.ceil(3.2))) # 올림
print("m.floor(3.2) = {0}".format(m.floor(3.2))) # 버림
print("m.pi = {0}".format(m.pi))