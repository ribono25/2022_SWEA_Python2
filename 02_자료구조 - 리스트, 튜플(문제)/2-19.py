# 연습문제 19

# 2-19.py

input_list = list(map(str, input().split(', ')))

var = len(input_list)

sorted_list = []
for _ in range(var):
    data = min(input_list)
    sorted_list.append(data)
    
    input_list.remove(data)

print(', '.join(map(str, sorted_list)))