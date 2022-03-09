# 연습문제 26

# 2-26.py

list1, list2 = [1,3,6,78,35,55], [12,24,35,24,88,120,155]

answer_list = []
for item in list1:
    for var in list2:
        if item == var:
            answer_list.append(item)
            break

print(answer_list)