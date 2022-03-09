# 연습문제 18

# 2-18.py

row, col = map(int, input().split(', '))

ans_list = []
for i in range(0, row):
    data_list = []

    for j in range(0, col):
        data_list.append(i * j)
    
    ans_list.append(data_list)

print(ans_list)