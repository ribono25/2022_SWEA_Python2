# 클래스 상속 5-13.py
class Parent:
    def __init__(self, family_name):
        self.__family_name = family_name
        print("Parent 클래스의 __init()__ ...")

    @property
    def family_name(self):
        return self.__family_name

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

child = Child("홍", "길동")

print(child.family_name)
print(child.first_name)
print(child.name)
print("=========>")
child.first_name = "이"
print(child.name)