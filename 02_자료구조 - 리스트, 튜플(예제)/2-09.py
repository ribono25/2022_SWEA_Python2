# 리스트 내포

# 2-09.py

data_list1 = [1,2,3,4,5]

print("data_list1: {0} {1}".format(type(data_list1), data_list1))

data_list2 = []
for item in data_list1:
    data_list2.append(item)

print("data_list2: {0} {1}".format(type(data_list2), data_list2))

data_list3 = [item for item in data_list1]
print("data_list3: {0} {1}".format(type(data_list3), data_list3))

data_list4 = data_list1
print("data_list4: {0} {1}".format(type(data_list4), data_list4))

print(data_list1 is data_list3)
print(data_list1 is data_list4)

print(hex(id(data_list1)))
print(hex(id(data_list3)))
print(hex(id(data_list4)))

data_list5 = []
for item in data_list1:
    if item % 2 == 1:
        data_list5.append(item)

print("data_list5: {0} {1}".format(type(data_list5), data_list5))

data_list6 = [item for item in data_list1 if item % 2 == 1]
print("data_list6: {0} {1}".format(type(data_list6), data_list6))

data_list7 = [item for item in data_list1 if item % 2 == 0]
print("data_list7: {0} {1}".format(type(data_list7), data_list7))

data_list8 = []
for x in data_list1:
    if x % 2 == 1:
        for y in data_list1:
            if y % 2 == 0:
                data_list8.append(x * y)

print("data_list8: {0} {1}".format(type(data_list8), data_list8))

data_list9 = [x * y for x in data_list1 if x % 2 == 1 for y in data_list1 if y % 2 == 0] #중첩 for문 가능
print("data_list9: {0} {1}".format(type(data_list9), data_list9))

data_str = 'Hello, Python!'
data_list10 = [item.lower() for item in data_str]
print("data_list10: {0} {1}".format(type(data_list10), data_list10))