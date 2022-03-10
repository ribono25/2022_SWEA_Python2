# 딕셔너리 내포

# 3-16.py

data_dict1 = {
    "홍길동" : 20, 
    "이순신" : 45,
    "강감찬" : 35
}
print("data_dict1: {0} {1}".format(type(data_dict1), data_dict1))

data_set1 = {item for item in data_dict1.items()}
print("\ndata_set1: {0} {1}".format(type(data_set1), data_set1))

data_dict2 = {key: data_dict1[key] for key in data_dict1} # 키: 값 for _ in _ 형태로 dict 객체 생성
print("\ndata_dict2: {0} {1}".format(type(data_dict2), data_dict2))

data_dict3 = {key: data_dict1[key] for key in data_dict1.keys()}
print("\ndata_dict3: {0} {1}".format(type(data_dict3), data_dict3))

data_dict4 = {item[0]: item[1] for item in data_dict1.items()}
print("\ndata_dict4: {0} {1}".format(type(data_dict4), data_dict4))

data_dict5 = {key: value for key, value in data_dict1.items()}
print("\ndata_dict5: {0} {1}".format(type(data_dict5), data_dict5))