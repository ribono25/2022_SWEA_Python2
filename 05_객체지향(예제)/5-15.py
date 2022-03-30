# 객체 오름차순/내림차순 정렬 5-15.py
# 객체 Student 생성 (name, gender, height)
# name, height 기준으로 정렬
# Student 조건
# 1. 프라이빗 필드를 가지고 있음
# 2. 읽기 전용 name, gender의 프로퍼티
# 3. 읽기, 쓰기 모두 가능한 height의 프로퍼티
# 4. 특수함수 __repr__에 대한 정의를 가짐

class Student:
    def __init__(self, name, gender, height):
        self.__name = name
        self.__gender = gender
        self.__height = float(height)
    
    @property
    def name(self):
        return self.__name
    
    @property
    def gender(self):
        return self.__gender

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height == height
    
    def __repr__(self):
        return f"Student(name: {self.name}, gender: {self.gender}, height: {self.height})"

members = [
    Student('홍길동', '남', 176.5),
    Student('이순신', '남', 188.5),
    Student('유관순', '여', 158.4),
    Student('강감찬', '남', 182.2)
]

for member in members:
    print(repr(member))

print("name으로 오름차순 정렬 후 ===>")
sorted_members = sorted(members, key = lambda x : x.name)
for member in sorted_members:
    print(repr(member))

print("name으로 내림차순 정렬 후 ===>")
sorted_members = sorted(members, key = lambda x : x.name, reverse = True)
for member in sorted_members:
    print(repr(member))

print("height으로 오름차순 정렬 후 ===>")
sorted_members = sorted(members, key = lambda x : x.height)
for member in sorted_members:
    print(repr(member))

print("height으로 내림차순 정렬 후 ===>")
sorted_members = sorted(members, key = lambda x : x.height, reverse = True)
for member in sorted_members:
    print(repr(member))