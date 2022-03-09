# 셋의 생성

# 3-01.py

data_set = {10, 20, '파이썬', '파이썬'} # 중복 삭제
print("{0} {1}".format(type(data_set), data_set))

data_set = set(range(10, 21, 2)) 
print("{0} {1}".format(type(data_set), data_set))

data_str = 'Better Tomorrow' 
data_set = set(data_str) # 순서 랜덤 / 중복 문자 삭제
print("{0} {1}".format(type(data_set), data_set))