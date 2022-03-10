# 딕셔너리 항목 접근

# 3-10.py

data_dict1 = {
    "홍길동":20,
    "이순신":45,
    "강감찬":35
}

print("data_dict1['홍길동'] => {0}".format(data_dict1["홍길동"])) # 객체 이름 + [키] => value

try:
    print("data_dict1['을지문덕'] => {0}".format(data_dict1["을지문덕"]))
except KeyError as k:
    print(k)