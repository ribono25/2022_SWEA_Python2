# 튜플 내포

# 2-15.py

data_tuple1 = (1,2,3,4,5)

print("data_tuple1: {0} {1}".format(type(data_tuple1), data_tuple1))

data_generator1 = (item for item in data_tuple1) # generator 클래스
print("data_genenrator1: {0} {1}".format(type(data_generator1), data_generator1))

data_tuple2 = tuple(data_generator1) # 리스트와 다른 점 : 내포 시 generator 클래스이기 때문에 tuple로 변환 要
print("data_tuple2: {0} {1}".format(type(data_tuple2), data_tuple2))

data_tuple3 = tuple(item for item in data_tuple1 if item % 2 == 1)
print("data_tuple3: {0} {1}".format(type(data_tuple3), data_tuple3))

data_tuple4 = tuple(item for item in data_tuple1 if item % 2 == 0)
print("data_tuple4: {0} {1}".format(type(data_tuple4), data_tuple4))

data_tuple5 = tuple(x * y for x in data_tuple1 if x % 2 == 1 for y in data_tuple1 if y % 2 == 0)
print("data_tuple5: {0} {1}".format(type(data_tuple5), data_tuple5))