class Number:
    def __init__(self,value):
        self .value = value
    def __add__(self,other):
        return self.value + other.value
a = Number(10)
b = Number(20)
print(a+b)
class Student:
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return self.name
s1 = Student("Anamika")
print(s1)
class Number:
    def __init__(self,value):
        self.value =value
    def __mul__(self,other):
        return self.value * other.value
a = Number(5)
b = Number(4)
print(a*b)
class Test:
    def __add__(self,other):
        return 100
a = Test()
b = Test()
print(a+b)
