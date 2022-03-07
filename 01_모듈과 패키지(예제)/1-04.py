# sys 모듈

# 1-04.py

import sys

print("sys.argv => {0} {1}".format(type(sys.argv), sys.argv)) 
# sys.argv : 리스트 타입, 명령행에서 python 명령에 전달된 인자들의 정보를 담고 있음

for i, val in enumerate(sys.argv):
    print("sys.argv[{0}] => {1}".format(i, val))

# configuration - parameters 에 값(1 2 3) 입력 시, sys.argv[1] = 1, sys.argv[2] = 2, sys.argv[3] = 3