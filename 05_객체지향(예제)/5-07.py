# 인스턴스 변수의 접근 제한 기능 5-07.py
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

        print(f'{self.__name} 객체가 생성되었습니다.')

    def __del__(self):
        print(f'{self.__name} 객체가 제거되었습니다.')

    def to_string(self):
        return "{0}\t{1}".format(self.__name, self.__age)

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        if age < 0:
            raise TypeError('나이는 0 이상의 값만 허용됩니다.')
        
        self.__age = age

members = [
    Person('홍길동', 20),
    Person('이순신', 40),
    Person('강감찬', 35)
]

members[0].set_age(-20)

for member in members:
    print(member.to_string())

a = members[1].get_name
print(a) # 외부 필드 접근 완전 제한