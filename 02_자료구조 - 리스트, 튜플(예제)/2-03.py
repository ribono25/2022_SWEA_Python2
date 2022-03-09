# 리스트 기본 연산

# 2-03.py

data_list1, data_list2 = [10,20,30], [40,50]

print("data_list1: {0} {1}".format(hex(id(data_list1)), data_list1))
print("data_list2: {0} {1}".format(hex(id(data_list2)), data_list2))

print("{0} + {1} => {2}".format(data_list1, data_list2, data_list1+data_list2)) # 덧셈 연산 가능

print("data_list1: {0} {1}".format(hex(id(data_list1)), data_list1)) # 덧셈 연산 이후에도 주소 & 원소 변동 X
print("data_list2: {0} {1}".format(hex(id(data_list2)), data_list2))

print("{0} * 2 => {1}".format(data_list1, data_list1 * 2)) # 곱셈 연산 가능
print("{0} * 2 => {1}".format(data_list2, data_list2 * 3))

print("data_list1: {0} {1}".format(hex(id(data_list1)), data_list1)) # 곱셈 연산 이후에도 주소 & 원소 변동 X
print("data_list2: {0} {1}".format(hex(id(data_list2)), data_list2))