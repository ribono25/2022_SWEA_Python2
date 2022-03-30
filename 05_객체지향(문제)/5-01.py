# 5-01.py
class Student:

    def __init__(self, kor, eng, math):
        self.__kor = kor
        self.__eng = eng
        self.__math = math
    
    def calsum(self):
        print(self.__kor + self.__eng + self.__math)

kor, eng, math = map(int, input().split(', '))
student = Student(kor, eng, math)

print("국어, 영어, 수학의 총점: ", end = "")
student.calsum()