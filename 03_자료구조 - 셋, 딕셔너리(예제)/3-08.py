# 리스트, 튜플, 셋의 변환

# 3-08.py

data_str = "Hello"

data_list = list(data_str)
print("{0} => {1} : {2}".format(type(data_str), type(data_list), data_list))

data_tuple = tuple(data_list)
print("{0} => {1} : {2}".format(type(data_list), type(data_tuple), data_tuple))

data_set = set(data_tuple)
print("{0} => {1} : {2}".format(type(data_tuple), type(data_set), data_set))

data_list = list(data_set)
print("{0} => {1} : {2}".format(type(data_set), type(data_list), data_list))