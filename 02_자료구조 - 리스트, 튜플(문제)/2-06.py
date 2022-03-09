# 연습문제 6

# 2-06.py

var = int(input())

answer_list = [i for i in range(1, var+1) if var % i == 0]
print(answer_list)