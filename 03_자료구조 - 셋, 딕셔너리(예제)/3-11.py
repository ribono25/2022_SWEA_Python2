# 딕셔너리 항목 추가

# 3-11.py

data_dict1 = {
    "홍길동" : 20, 
    "이순신" : 45,
    "강감찬" : 35
}

print("data_dict1: {0} {1}".format(type(data_dict1), data_dict1))

data_dict1["을지문덕"] = 40 # 객체 이름[미중복 key] = value
print("data_dict1: {0} {1}".format(type(data_dict1), data_dict1))

data_dict1.update({"신사임당":50, "유관순":16}) # update() 함수에 dict 객체 전달
print("data_dict1: {0} {1}".format(type(data_dict1), data_dict1))