# 문자열 구성 확인 4-13.py

data_str = "10, 20, 3o, 40, 50"

data_str = data_str.replace(" ", "")
print(data_str)

data_list = data_str.split(",")
for val in data_list:
    print(val, end= " ")
    if not val.isdigit():
        print("<= ", end="")
    print()