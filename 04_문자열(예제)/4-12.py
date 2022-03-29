# 문자열 자르기 4-12.py

data_str = "10, 20, 30, 40, 50"

data_str = data_str.replace(" ", "")
print(data_str)

data_list = data_str.split(",")
for val in data_list:
    print(val)