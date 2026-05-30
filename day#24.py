class Student:
    def __init__(self):
        print("Object Created")
s1 = Student()
class Student:
    def __str__(self):
        return "Student Object"
s1 = Student()
print(s1)
class MyData:
    def __len__(self):
        return 100
obj = MyData()
print(len(obj))
class Number:
    def __init__(self,value):
        self.value = value
    def __add__(self,other):
        return self.value +other.value
a = Number(10)
b = Number(20)
print(a+b)
