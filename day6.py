def greet():
    print("hello")  
greet()          
def add():
    a=10
    b=20
    print(a+b)
add()
def table():
    num = int (input("enter number:"))
    for i in range (1,11):
        print(num,"x",i,"=",num*i)
table()
def square():
    num = int(input("enter your number:"))
    print(num*num)
square()
def name(aname,bname):
    print("hello",aname,bname)
name("sam","willam")
def greet(name):
    print("Hello",name)
greet("Anamika")
def add(a,b):
    return a+b
result = add(2,3)
print(result)
def greet(name="guest"):
    print("hello",name)
greet()
greet("anamika")
def student(name,age):
    print(name,age)
student(age=18,name="anamika")
def add (a,b):
    print(a+b)
add(2,3)
def numbers(*args):
    print(args)
numbers(1,2,3,4)
def info (**kwargs):
    print(kwargs)
info(name="Anamika",age=18)
