# 메서드 오버라이딩 5-14.py
class Parent:
    def __init__(self, family_name):
        self.__family_name = family_name
        print("Parent 클래스의 __init()__ ...")

    @property
    def family_name(self):
        return self.__family_name

    def print_info(self):
        print("Parent : {0}".format(self.family_name))

class Child(Parent):
    def __init__(self, first_name, last_name):
        Parent.__init__(self, last_name)
        # super().__init__(last_name)
        self.__first_name = first_name
        print("Child 클래스의 __init()__ ...")

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name):
        self.__first_name = first_name
    
    @property
    def name(self):
        return f"{self.family_name} {self.first_name}"

    def print_info(self):
        Parent.print_info(self)
        # super().print_info()
        print(f"Child: {self.name}")

child = Child('길동', '홍')
child.print_info()