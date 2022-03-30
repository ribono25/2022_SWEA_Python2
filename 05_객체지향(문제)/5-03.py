# 5-03.py
class Student():
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

class GraduateStudent(Student):
    def __init__(self, name, major):
        Student.name = name
        self.__major = major
    
    @property
    def major(self):
        return self.__major
    
student = Student('홍길동')
print('이름: {0}'.format(student.name))

Gstudent = GraduateStudent('이순신', '컴퓨터')
print('이름: {0}, 전공: {1}'.format(Gstudent.name, Gstudent.major)) 