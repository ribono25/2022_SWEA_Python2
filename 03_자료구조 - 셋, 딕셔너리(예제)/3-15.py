# 딕셔너리와 for 문

# 3-15.py

data_dict1 = {
    "홍길동" : 20, 
    "이순신" : 45,
    "강감찬" : 35
}
print("data_dict1: {0} {1}".format(type(data_dict1), data_dict1))

print("{0} {1}".format(type(data_dict1.items()), data_dict1.items())) # 튜플
print("{0} {1}".format(type(data_dict1.keys()), data_dict1.keys())) # 문자열
print("{0} {1}".format(type(data_dict1.values()), data_dict1.values())) # 정수

print()
for key in data_dict1: # 각 항목의 키는 변수 key에 저장
    print("key, data_dict1[key] => '{0}', {1}".format(key, data_dict1[key]))

print()
for key in data_dict1.keys(): # 위와 동일
    print("key, data_dict1[key] => '{0}', {1}".format(key, data_dict1[key]))

print()
for item in data_dict1.items(): # 각 항목이 변수 item에 튜플 형식으로 저장, item[0] : key & item[1] : value
    print("item[0], item[1] => '{0}', {1}".format(item[0], item[1]))

print()
for key, value in data_dict1.items():
    print("key, value => '{0}', {1}".format(key, value))

print()
for value in data_dict1.values(): # 각 항목의 value가 변수 value에 저장
    print("value => {0}".format(value))