class Animal:
    def eat(self):
        print("Animal can eat")
class Dog(Animal):
    def bark(self):
        print("dog can bark")
class Puppy(Dog):
    def weep(self):
        print("puppy can weep")
p = Puppy() 

p.eat()   # from Animal
p.bark()  # from Dog
p.weep()  # from Puppy

class A:
    def __init__(self):
        print("A Constructor")
class B(A):
    def __init__(self):
        super(). __init__()
        print("B constructor")
class C(B):
    def __init__(self):
        super().__init__()
        print("C Constructor")
obj = C()

print(Puppy.mro())

class A:
    def show_A(self):
        print("Class A")

# Hierarchical inheritance
class B(A):
    def show_B(self):
        print("Class B")
class C(A):
    def show_C(self):
        print("class C")

# Multiple inheritance
class D(B,C):
    def show_D(self):
        print("class D")

obj = D()
obj.show_A()
obj.show_B()
obj.show_C()
obj.show_D()
print(D.mro())
class Animal:
    def eat(self):
        print("Animal can eat")
class Dog(Animal):
    def bark(self):
        print("Dog can bark")
class Cat(Animal):
    def meow(self):
        print("Cat can meow")

d = Dog()
c = Cat()

d.eat()   # inherited from Animal
d.bark()  

c.eat()   # inherited from Animal
c.meow()


