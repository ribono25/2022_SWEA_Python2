# 셋 항목 제거

# 3-04.py

data_set = set(range(1, 11))

print("data_set: {0}".format(data_set))

data_set.remove(9)
data_set.remove(2) # .remove(value) -> value 제거
print("data_set: {0}".format(data_set))

data_set.pop() # .pop -> 첫 번째 항목 제거
print("data_set: {0}".format(data_set))

data_set.clear() # .clear() -> 초기화
print("data_set: {0}".format(data_set)) # {}는 딕셔너리의 리터럴이므로 set()으로 표현함