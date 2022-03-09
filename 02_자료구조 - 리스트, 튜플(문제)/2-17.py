# 연습문제 17

# 2-17.py

from math import pi

data_list = list(map(int, input().split(', ')))

ans_list = []
for i in data_list:
    ans = i * 2 * pi
    ans_list.append(ans)

print(', '.join(format(x, ".2f") for x in ans_list))