# 셋 항목 추가

# 3-03.py

data_set = {1, 2, 3}

print("data_set: {0}".format(data_set))

data_set.add(3)
data_set.add(4) # .add -> 하나 추가

print("data_set: {0}".format(data_set))

data_set.update({4,5,6}) # .update -> 여러 개 추가
print("data_set: {0}".format(data_set))