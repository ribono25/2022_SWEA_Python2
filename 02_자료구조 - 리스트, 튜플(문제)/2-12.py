# 연습문제 12

# 2-12.py

answer_list = [i ** 2 for i in range(1, 21) if not (i % 3 == 0 and i % 5 == 0)]
print(answer_list)