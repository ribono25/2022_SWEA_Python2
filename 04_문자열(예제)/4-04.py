# 문자열의 범위 선택 4-04.py

data_str = "와우! 안녕하세요, 파이썬입니다."

start = input("시작 인덱스를 입력하세요: ")
end = input("종료 인덱스를 입력하세요: ")

try:
    start = int(start)
except ValueError:
    start = None

try:
    end = int(end)
except ValueError:
    end = None

print(f"'{data_str[start: end]}'")