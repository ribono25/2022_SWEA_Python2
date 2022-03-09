# 셋 항목 확인

# 3-05.py

data_set1 = {1,2,3,4,5}
data_set2 = {2,3}

print("3 in data_set1 => {0}".format(3 in data_set1))
print("6 not in data_set1 => {0}".format(6 not in data_set1))

print("{0}.issuperset({1}) => {2}".format(data_set1, data_set2, data_set1.issuperset(data_set2))) # a.issuperset(b) -> a가 b를 포함하는가?
print("{0}.issubset({1}) => {2}".format(data_set2, data_set1, data_set2.issubset(data_set1))) # a.issubset(b) -> a가 b에 포함되는가?