# 3-08.py

input_string = input()

upper, lower = 0, 0
for ch in input_string:
    if ch.isalpha():
        if ch.isupper():
            upper += 1
        else:
            lower += 1

print(f'UPPER CASE {upper}\nLOWER CASE {lower}')