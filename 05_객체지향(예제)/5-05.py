# 인스턴스 메서드 정의
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

        print(f'{self.name} 객체가 생성되었습니다.')

    def __del__(self):
        print(f'{self.name} 객체가 제거되었습니다.')

    def to_string(self): # 인스턴스 메서드
        return "{0}\t{1}".format(self.name, self.age)

members = [
    Person('홍길동', 20),
    Person('이순신', 40),
    Person('강감찬', 35)
]

for member in members:
    print(member.to_string())