# from ~ import ~ 문을 이용한 선택적 로딩

# 1-03.py

# from math import * -> 모든 함수, 값 참조
from math import radians, ceil, floor, pi # math 모듈이 로딩되지 않고 직접 로딩 (모듈명 X)
# from 모듈명 import

print("radians(90) = {0}".format(radians(90)))
print("ceil(3.2) = {0}".format(ceil(3.2))) # 올림
print("floor(3.2) = {0}".format(floor(3.2))) # 버림
print("pi = {0}".format(pi))