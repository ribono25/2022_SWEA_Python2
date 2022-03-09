# 셋 기본 연산

# 3-02.py

data_set1 = {1,2,3,4,5,6,7,11}
data_set2 = {2,3,5,9,11,12,15}

print("교집합 : {0}".format(data_set1 & data_set2)) # 교집합 기호 &
print("합집합 : {0}".format(data_set1 | data_set2)) # 합집합 기호 |
print("차집합 : {0}".format(data_set1 - data_set2)) # 차집합 기호 -

print("교집합 : {0}".format(data_set1.intersection(data_set2))) # 위와 동일
print("합집합 : {0}".format(data_set1.union(data_set2)))
print("차집합 : {0}".format(data_set1.difference(data_set2)))