# 딕셔너리 항목 변경

# 3-12.py

data_dict1 = {
    "홍길동" : 20, 
    "이순신" : 45,
    "강감찬" : 35
}

data_dict1["강감찬"] = 38 # 값 변경
print("data_dict1: {0} {1}".format(type(data_dict1), data_dict1))

data_dict1.update({"홍길동":25, "이순신":48}) # 중복된 키가 있을 때 value 변경
print("data_dict1: {0} {1}".format(type(data_dict1), data_dict1))