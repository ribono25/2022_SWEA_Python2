# 클래스 정의 및 객체 생성 5-03.py
class Person:
    pass

member = Person() # member 객체 생성

if isinstance(member, Person):
    print('member는 Person 클래스의 인스턴스입니다.')