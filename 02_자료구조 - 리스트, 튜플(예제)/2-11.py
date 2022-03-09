# 튜플 항목 접근

# 2-11.py

data_tuple = (10,20,30,40,50)

print("data_tuple: {0}".format(data_tuple))

print("data_tuple[0] => {0}".format(data_tuple[0]))
print("data_tuple[1] => {0}".format(data_tuple[1]))
print("data_tuple[2] => {0}".format(data_tuple[2]))
print("data_tuple[3] => {0}".format(data_tuple[3]))
print("data_tuple[4] => {0}".format(data_tuple[4]))

print("data_tuple[-5] => {0}".format(data_tuple[-5]))
print("data_tuple[-4] => {0}".format(data_tuple[-4]))
print("data_tuple[-3] => {0}".format(data_tuple[-3]))
print("data_tuple[-2] => {0}".format(data_tuple[-2]))
print("data_tuple[-1] => {0}".format(data_tuple[-1]))

try:
    print(data_tuple[5])
except IndexError as I:
    print(I)

print("data_tuple[0:3] => {0}".format(data_tuple[0:3]))
print("data_tuple[-5:-2] => {0}".format(data_tuple[-5:-2]))

print("data_tuple.index(20) => {0}".format(data_tuple.index(20)))