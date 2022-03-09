# 연습문제 25

# 2-25.py

input_list = [12, 24, 35, 70, 88, 120, 155]
input_list = [item for idx, item in enumerate(input_list) if not(idx == 0 or idx == 4 or idx == 5) ]

print(input_list)