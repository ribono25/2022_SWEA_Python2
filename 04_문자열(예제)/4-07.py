# 문자열 찾기 4-07.py

data_str = "파이썬은 클래스를 이용해 객체를 생성하는 객체지향 프로그래밍 언어입니다."

print(f"'{data_str}'")
input_str = input("위에서 찾고자하는 문자열을 입력하세요: ")

print("str.find() ...")
idx = data_str.find(input_str)
# idx = data_str.rfind(input_str) -> 오른쪽에서 왼쪽 진행


if not idx == -1:
    print(f"\t'{input_str}' : [{idx}] <= 문자열을 가장 먼저 찾은 위치")
else:
    print(f"\t'{input_str}'를 찾을 수 없습니다.")

print("str.index() ...")
try:
    idx = data_str.index(input_str)
    print(f"\t'{input_str}' : [{idx}] <= 문자열을 가장 먼저 찾은 위치")
except ValueError: # find는 -1, index는 ValueError
    print(f"\t'{input_str}'를 찾을 수 없습니다.")