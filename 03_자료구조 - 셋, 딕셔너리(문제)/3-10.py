# 3-10.py

input_string = input()
ans_list = [0 for _ in range(0, 26)]

for c in input_string:
    ans_list[ord(c) - 97] += 1

for idx, item in enumerate(ans_list):
    if item == 0:
        continue

    print(f'{chr(idx+97)},{item}')