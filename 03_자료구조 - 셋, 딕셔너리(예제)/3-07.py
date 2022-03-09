# 셋 내포

# 3-07.py

data_set1 = {1,2,3,4,5}
print("data_set1: {0} {1}".format(type(data_set1), data_set1))

data_set2 = {item for item in data_set1}
print("data_set2: {0} {1}".format(type(data_set2), data_set2))

data_set3 = {item for item in data_set1 if item % 2 == 1}
print("data_set3: {0} {1}".format(type(data_set3), data_set3))

data_set4 = {item for item in data_set1 if item % 2 == 0}
print("data_set4: {0} {1}".format(type(data_set4), data_set4))

data_set5 = {x * y for x in data_set1 if x % 2 == 1 for y in data_set1 if y % 2 == 0}
print("data_set5: {0} {1}".format(type(data_set5), data_set5))