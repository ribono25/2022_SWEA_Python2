# 문자열을 마스크 문자열로 치환하기 4-14.py

data = "파이썬은 클래스를 이용해 객체를 생성하는 객체지향 프로그래밍 언어입니다."

print(f"'{data}'")

masking_str = input("마스킹할 문자열을 입력하세요: ")
find_str = input("찾을 문자열을 입력하세요: ")

idx, cnt = -1, 1
while True:
    idx = data.find(find_str, idx+1)

    if idx == -1:
        break

    print(f'[{idx}] ~ [{idx+len(find_str)-1}]')
    newdata = data.replace(find_str, masking_str, cnt)

    print(newdata)

    idx = idx+len(find_str)
    cnt += 1
