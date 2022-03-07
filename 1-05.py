# random 모듈의 활용

# 1-05.py

from random import random, uniform, randrange, choice, choices, sample, shuffle

print("random() => {0}".format(random())) # 0 <= N <= 1 범위의 실수인 난수 N 반환

print("uniform({0}, {1}) => {2}".format(1.0, 10.0, uniform(1.0, 10.0))) # random 범위 확장 ver

print("randrange({0}, {1}) => {2}".format(1, 45, randrange(1, 45))) # 1 <= N < 45 범위의 정수인 난수 N 반환
print("randrange({0}) => {1}".format(45, randrange(45))) # 0 <= N < 45 범위의 정수인 난수 N 반환
print("randrange({0}, {1}, {2}) => {3}".format(1, 45, 2, randrange(1, 45, 2))) # 1 <= N < 45 중 홀수인 난수 N 반환
# start 생략 : 0 기본값 / step 생략 : 1 기본값

data_list = [1,2,3,4,5]
print("choice({0}) => {1}".format(data_list, choice(data_list))) # 시퀸스 객체 중 임의 항목 반환
print("choices({0}, {1}) => {2}".format(data_list, 'k=2', choices(data_list, k=2))) # 임의의 k개 반환 (k=n 의 꼴)
print("sample({0}, {1}) => {2}".format(data_list, 'k=2', sample(data_list, k=2))) # 시퀸스 객체/set 객체 중 임의의 k개 반환 + 겹침X

shuffle(data_list) # 시퀸스 객체의 항목을 뒤섞음, 반환값X
print("data_list => {0}".format(data_list))