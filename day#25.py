class Parent:
    def show(self):
        print("Parent Method")
class Child(Parent):
    def  show(self):
        print("Child Method")
c1 = Child()
c1.show()
class Parent:
    def show(self):
        print("Parent Method")
class Child(Parent):
    def show(self):
        super().show()
        print("Child Method")
c1 = Child()
c1.show()
class Animal:
    def sound(self):
        print("Animal Sound")
class Dog(Animal):
    def sound(self):
        print("Bark Bark")
d1 = Dog()
d1.sound()
class A:
    def hello(self):
        print("A")
class B(A):
    def hello(self):
        print("B")
obj = B()
obj.hello()