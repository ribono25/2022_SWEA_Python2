# 5-05.py
class Rectangle:
    def __init__(self, width, length):
        self.__width = width
        self.__length = length
    
    def cal(self):
        self.__area = self.__width * self.__length
    
    def calprint(self):
        print(f'사각형의 면적: {self.__area}')

r = Rectangle(4, 5)
r.cal()
r.calprint()