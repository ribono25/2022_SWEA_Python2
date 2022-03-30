# 5-04.py
class Circle:
    s = 0

    def __init__(self, radius):
        self.__radius = radius

    def cal(self):
        Circle.s = self.__radius * self.__radius * 3.14
    
    @classmethod
    def calprint(cls):
        print(f'원의 면적: {cls.s:.2f}')

circle = Circle(2)
circle.cal()
circle.calprint()