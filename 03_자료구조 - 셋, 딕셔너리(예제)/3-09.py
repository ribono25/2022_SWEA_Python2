# 딕셔너리의 생성

# 3-09.py

data_dict1 = {
    "홍길동" : 20, # 키: 값의 쌍으로 기술
    "이순신" : 45,
    "강감찬" : 35
}

print("data_dict1: {0} {1}".format(type(data_dict1), data_dict1))

data_dict2 = dict(홍길동=20, 이순신=45, 강감찬=35) # key를 문자열로 기술하지 않도록 주의
print("data_dict2: {0} {1}".format(type(data_dict2), data_dict2))

data_tuple = (("홍길동",20), ("이순신",45), ("강감찬",35)) # (키, 값)으로 구성된 튜플을 항목으로 하는 튜플
data_dict3 = dict(data_tuple)

print("data_dict3: {0} {1}".format(type(data_dict3), data_dict3))

data_list = list(data_tuple) # 리스트 & set 도 가능
data_set = set(data_tuple)
data_dict4 = dict(data_list)
data_dict5 = dict(data_set)

print("data_dict4: {0} {1}".format(type(data_dict4), data_dict4))
print("data_dict5: {0} {1}".format(type(data_dict5), data_dict5))