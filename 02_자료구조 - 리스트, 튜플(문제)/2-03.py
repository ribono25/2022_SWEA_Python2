# 연습문제 3

# 2-03.py

answer_list = []

for i in range(2, 10):
    data_list = [i * j for j in range(1, 10) if not(i * j % 3 == 0 or i * j % 7 == 0)]
    answer_list.append(data_list)

print(answer_list)