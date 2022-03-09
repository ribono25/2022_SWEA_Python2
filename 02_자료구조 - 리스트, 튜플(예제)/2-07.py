# 리스트 항목 확인

# 2-07.py

data_list = list(range(10, 90, 10)) 

print("50 in data_list => {0}".format(50 in data_list)) # value in list : value가 list에 존재하는지 검사(True or False)
print("50 not in data_list => {0}".format(50 not in data_list)) # in 연산에 not 연산

print("data_list.count(50) => {0}".format(data_list.count(50))) # list.count(value) : value가 list에 몇 개 존재하는지 반환