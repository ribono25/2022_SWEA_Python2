# 튜플 항목 확인

# 2-13.py

data_tuple = tuple(range(10, 90, 10))

print("50 in data_tuple => {0}".format(50 in data_tuple))
print("50 not in data_tuple => {0}".format(50 not in data_tuple))

print("data_tuple.count(50) => {0}".format(data_tuple.count(50)))
print("data_tuple.count(55) => {0}".format(data_tuple.count(55)))