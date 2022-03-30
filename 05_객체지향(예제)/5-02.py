# 딕셔너리 객체의 생성 및 정보 출력

def create(name, age):
    return {'name' : name, 'age' : age}

def to_string(person):
    print('{0}\t{1}'.format(person['name'], person['age']))

members = [
    create('홍길동', 20),
    create('이순신', 40),
    create('강감찬', 35)
]

for member in members:
    to_string(member)