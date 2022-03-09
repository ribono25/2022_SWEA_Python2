# 리스트 생성

# 2-01.py

data_list = [10, 21.5, '파이썬', True] # 각기 다른 형의 원소를 가질 수 있음

print("{0} {1}".format(type(data_list), data_list))

data_list = list(range(10, 21, 2)) # 10~20까지 공차가 2인 등차수열을 갖는 리스트

print("{0} {1}".format(type(data_list), data_list))

data_list = list('안녕하세요') # 개별 문자를 원소로 하는 리스트

print("{0} {1}".format(type(data_list), data_list))