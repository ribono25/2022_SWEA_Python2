# 5-06.py
class Shape:
    def area(self):
        return 0

class Sqaure(Shape):
    def __init__(self, length):
        self.__length = length
    
    def area(self):
        return self.__length * self.__length

square = Sqaure(3)
print('정사각형의 면적: {0}'.format(square.area()))