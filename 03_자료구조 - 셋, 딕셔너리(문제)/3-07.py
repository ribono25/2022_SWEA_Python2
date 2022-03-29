# 3-07.py

input_str = input() 

lett, dig = 0, 0
for ch in input_str:
    if ch.isalpha():
        lett += 1
    elif ch.isdigit():
        dig += 1

print(f'LETTERS {lett}\nDIGITS {dig}')