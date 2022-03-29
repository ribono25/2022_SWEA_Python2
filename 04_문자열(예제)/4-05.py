# 문자열 출현 횟수 확인 4-05.py

data_str = "Have a nice day!"

print(f"'{data_str}'")
input_str = input("위에서 찾고자하는 문자열을 입력하세요: ")

print(f"'{data_str}에서 '{input_str}'은(는) {data_str.count(input_str)}번 나타납니다.")