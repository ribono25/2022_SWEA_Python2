# 멤버 필드의 접근 제한이 이루어지지 않을 경우 5-06.py
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

        print(f'{self.name} 객체가 생성되었습니다.')

    def __del__(self):
        print(f'{self.name} 객체가 제거되었습니다.')

    def to_string(self):
        return "{0}\t{1}".format(self.name, self.age)


# self.__name = name → 프라이빗 필드 생성
# getter(읽어오는 메서드)/setter(변경하는 메서드) 메서드의 제공 여부 판단