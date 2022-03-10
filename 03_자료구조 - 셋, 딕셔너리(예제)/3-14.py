# 딕셔너리 항목 확인

# 3-14.py

data_dict1 = {
    "홍길동" : 20, 
    "이순신" : 45,
    "강감찬" : 35
}
print("data_dict1: {0} {1}".format(type(data_dict1), data_dict1))

print("'홍길동' in data_dict1 => {0}".format("홍길동" in data_dict1)) # 해당 key를 가진 항목이 있는지 검사
print("'신사임당' in data_dict1 => {0}".format("신사임당" not in data_dict1))