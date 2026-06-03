class Father:
    def father_method(self):
        print("Father's method")
class Mother:
    def mother_method(self):
        print("Mother's method")
class Child(Father,Mother):
    pass
c = Child()
c.father_method()
c.mother_method()
class A:
    def show(self):
        print("A")
class B:
    def show(self):
        print("B")
class C(A,B):
    pass
obj = C()
obj.show()
print(C.mro())
class A:
    def show(self):
        print("A")
class B(A):
    def show(self):
        print("B")
        super().show()
class C(A):
    def show(self):
        print("C")
        super().show()
class D(B,C):
    def show(self):
        print("D")
        super().show()
d = D()
d.show()
print(D.mro())
class LoggerMixin:
    def log(self,message):
        print(f"LOg: {message}")
class User(LoggerMixin):
    pass
u = User()
u.log("User created")