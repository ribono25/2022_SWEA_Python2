# 딕셔너리 항목 제거

# 3-13.py

data_dict1 = {
    "홍길동" : 20, 
    "이순신" : 45,
    "강감찬" : 35,
    "을지문덕" : 40
}
print("data_dict1: {0} {1}".format(type(data_dict1), data_dict1))

del data_dict1["강감찬"] # del 객체 이름[key]
print("data_dict1: {0} {1}".format(type(data_dict1), data_dict1))

data_dict1.pop("이순신") # del data_dict["이순신"] 과 동일
print("data_dict1: {0} {1}".format(type(data_dict1), data_dict1))

data_dict1.clear()
print("data_dict1: {0} {1}".format(type(data_dict1), data_dict1))