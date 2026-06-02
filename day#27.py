class Parent:
    def show(self):
        print("I am Parent")
class Child(Parent):
    pass
c1 = Child()
c1.show()
class Animal:
    def sound(self):
        print("Animal makes sound")
class Dog(Animal):
    def bark(self):
        print("Dog barks")
d1 = Dog()
d1.sound()
d1.bark()
class Parent:
    def __init__(self):
        print("Parent constuctor")
class Child(Parent):
    pass
c1 = Child()
class A:
    def hello(self):
        print("Hello")
class B(A):
    pass 
obj = B()
obj.hello()

