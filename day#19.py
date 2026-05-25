def decorator(func):
    def wrapper():
        print("Before Function")
        func()
        print("After Function")
    return wrapper
@decorator
def hello():

    print("Hello Python")
hello()
def smart(func):
    def inner():
        print("welcome")
        func()
    return inner
@smart
def name():
    
    print("Anamika")
name()
def login_required(func):
    def wrapper():
        print("User verifield")
        func()
    return wrapper
@login_required
def profile():

    print("Welcome Profile")
profile()
import time
def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(end-start)
    return wrapper
@timer
def work():

    print("working...")
work()
def log(func):
    def wrapper():
        print("Function Started")
        func()
        print("Function Ended")
    return wrapper
@log 
def hello():

    print("Hello")
hello()
def admin_only(func):
    def wrapper():
        print("Admin Access Granted")
        func()
    return wrapper
@admin_only
def dashboard():

    print("Dashboard Open")
dashboard()
class Student:
    def __init__(self,name):
        self .__name = name
    def get_name(self):
        return self .__name
s1 = Student("Anamika")
print(s1.get_name()) 
class Student:
    def __init__(self,name):
        self .__name = name
    def set_name(self,name):
        self .__name = name
    def get_name(self):
        return self.__name
s1 = Student("Anamika")   
s1.set_name("python Girl")
print(s1.get_name())
