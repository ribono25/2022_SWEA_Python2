# 튜플의 생성

# 2-10.py

data_tuple = (10, 21.5, '파이썬', True) # 다른 자료형 가능

print("{0} {1}".format(type(data_tuple), data_tuple))

data_tuple = tuple(range(10, 21, 2))
print("{0} {1}".format(type(data_tuple), data_tuple))

data_str = '안녕하세요'
data_tuple = tuple(data_str) # 개별 원소 저장됨
print("{0} {1}".format(type(data_tuple), data_tuple))