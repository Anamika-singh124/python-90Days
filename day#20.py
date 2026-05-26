class Parent:
    def show(self):
        print("Parent Class")
class Child(Parent):
    pass
c1 = Child()
c1.show()
class Animal:
    def sound(self):
        print("Animal Sound")
class Dog(Animal):
    def bark(self):
        print("Dog bark")
d1 = Dog()
d1.sound()
d1.bark()
class A:
    def show(self):
        print("A")
class B(A):
    pass
class C(B):
    pass
c1 = C()
c1.show()
class Parent:
    def show(self):
        print("Parent")
class Child(Parent):
    def show(self):
        print("Child")
c1 = Child()
c1.show()
class Student:
    def __init__(self):
        self.name ="Anamika"
s1 = Student()
print(s1.name)
class Student:
    def __init__(self):
        self._age = 18
s1 = Student()
print(s1._age)
class Student:
    def __init__(self):
        self .__marks = 95
    def show(self):
        print(self.__marks)
s1 = Student()
s1.show()


