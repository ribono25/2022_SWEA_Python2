# 튜플 기본 연산

# 2-12.py

data_tuple1, data_tuple2 = (10,20,30), (40,50)

print("data_tuple1: {0} {1}".format(hex(id(data_tuple1)), data_tuple1))
print("data_tuple2: {0} {1}".format(hex(id(data_tuple2)), data_tuple2))

print("{0} + {1} => {2}".format(data_tuple1, data_tuple2, data_tuple1+data_tuple2)) # 덧셈 연산 가능

print("data_tuple1: {0} {1}".format(hex(id(data_tuple1)), data_tuple1))
print("data_tuple2: {0} {1}".format(hex(id(data_tuple2)), data_tuple2))

print("{0} * 2 => {1}".format(data_tuple1, data_tuple1 * 2)) # 곱셈 연산 가능
print("{0} * 3 => {1}".format(data_tuple2, data_tuple2 * 3))

print("data_tuple1: {0} {1}".format(hex(id(data_tuple1)), data_tuple1))
print("data_tuple2: {0} {1}".format(hex(id(data_tuple2)), data_tuple2))

