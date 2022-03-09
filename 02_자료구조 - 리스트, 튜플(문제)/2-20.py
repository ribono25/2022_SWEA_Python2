# 연습문제 20

# 2-20.py

input_list = list(map(int, input().split(', ')))

answer_list = [item for item in input_list if item % 2 == 1]
print(', '.join(map(str, answer_list)))