# 클래스 메서드의 사용 5-10.py
class Person:
    count = 0

    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        Person.count += 1
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

    @classmethod
    def get_info(cls):
        return "현재 Person 클래스의 인스턴스는 {0}개 입니다.".format(cls.count)

members = [
    Person('홍길동', 20),
    Person('이순신', 40),
    Person('강감찬', 35)
]

print(Person.get_info())