# 데코레이터 기능 5-08.py
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

        print(f'{self.__name} 객체가 생성되었습니다.')

    def __del__(self):
        print(f'{self.__name} 객체가 제거되었습니다.')

    def to_string(self):
        return "{0}\t{1}".format(self.__name, self.__age)

    @property
    def name(self):
        return self.__name
    
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age < 0:
            raise TypeError('나이는 0 이상의 값만 허용됩니다.')
        self.__age = age

members = [
    Person('홍길동', 20),
    Person('이순신', 40),
    Person('강감찬', 35)
]
    
members[0].age = 22

for member in members:
    print(member.to_string())