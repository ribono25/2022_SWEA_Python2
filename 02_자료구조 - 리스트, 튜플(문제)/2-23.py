# 연습문제 23

# 2-23.py

data_list = [12, 24, 35, 70, 88, 120, 155]
data_list = [item for idx, item in enumerate(data_list) if (idx+1) % 2 == 0]
print(data_list)