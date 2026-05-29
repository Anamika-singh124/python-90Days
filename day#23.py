name = "Python"
print(dir(name))
import math 
print(dir(math))
class Student:
    def __init__(self,name):
        self.name = name
s1 = Student("Anamika")
print(s1.__dict__)
class Car:
    brand = "BMW"
print(Car.__dict__)
class Parent:
    def   __init__(self):
        print("parent constructor")
class Child(Parent):
    def __init__(self):
        super().__init__()
        print("CHild constructor")
c1 = Child()
class Parent:
    def __init__(self,name):
        self.name = name
class Child(Parent):
    def __init__(self,name):
        super(). __init__(name)
c1 = Child("anamika")
print(c1.name)

