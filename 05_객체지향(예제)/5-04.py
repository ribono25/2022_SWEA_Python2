# 객체의 생성과 소멸, 그리고 self
class Person:
    def __init__(self, name, age): # 생성자, self → 객체 공간을 가리킴
        self.name = name
        self.age = age

        print(f'{self.name} 객체가 생성되었습니다.')

    def __del__(self): # 소멸자
        print(f'{self.name} 객체가 제거되었습니다.')

member = Person("홍길동", 20)

print('{0}\t{1}'.format(member.name, member.age))
print(dir(member))