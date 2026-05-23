a = 10
b = 10
print(a == b)
a = [1,2]
b = [1,2]
print(a == b)
print(a is b)
a = b = [1,2]
print(a is b)
class student:
    name = "Anamika"
obj = student()
print(obj.name)
class student:
    def hello(self):
        print("Hello student")
obj = student()
obj.hello()
class Student:
    def __init__(self,name):
        self.name = name
obj = Student("Anamika")
print(obj.name)
class Student:
     name = "Anamika"
obj = Student()
print(obj.name)
class student:
    college = "lpu"
s1 = student()
s2 = student()
print(s1.college)
print(s2.college)
class student:
    def __init__(self,name):
        self.name = name
s1 = student("Anamika")
print(s1.name)
class Mobile:
    brand = "Samsung"
m1 = Mobile()
print(m1.brand)
class Dog:
    def sound(self):
        print("Bark")
d1 = Dog()
d1.sound()

