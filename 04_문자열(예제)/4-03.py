# 문자의 선택 4-03.py

data_str = "안녕하세요, 파이썬입니다."

idx = 0
cnt = len(data_str)

while True:
    print(f"data_str[{idx}] : {data_str[idx]}")

    if idx == cnt-1:
        break

    idx += 1

print("-" * 20)


idx = -1

while True:
    print(f"data_str[{idx}] : {data_str[idx]}")
    if idx == -cnt:
        break

    idx -= 1