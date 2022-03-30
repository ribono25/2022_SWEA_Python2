# 딕셔너리 및 리스트 객체를 이용한 코드 생성 5-01.py

members = [
    {'name' : '홍길동', 'age' : 20},
    {'name' : '이순신', 'age' : 40},
    {'name' : '강감찬', 'age' : 35}
]

for member in members:
    print('{0}\t{1}'.format(member['name'], member['age']))