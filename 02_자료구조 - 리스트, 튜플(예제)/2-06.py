# 리스트 항목 제거

# 2-06.py

data_list = list(range(10, 110, 10))

del data_list[2]
print("data_list: {0}".format(data_list))

del data_list[3:5] # del list[index]
print("data_list: {0}".format(data_list))

data_list.pop(5) # list.pop(index)
print("data_list: {0}".format(data_list))

data_list.remove(100) # list.remove(value)
print("data_list: {0}".format(data_list))

data_list.clear() # 모든 항목 제거 => del data_list[:]
print("data_list: {0}".format(data_list))