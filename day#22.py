class Student:
    college = "LPU"

    @classmethod
    def show(cls):

        print(cls.college)
Student.show()        
class Student:
      college = "LPu"

      @classmethod
      def change(cls):
          
          cls.college = "LPU"
      
Student.change()    

print(Student.college)

class Student:
    def hello(self):
        print("Hello")
class Student:
    @classmethod
    def hi(cls):

        print("hi")
class Student:
    def __init__(self,name):

        self.name = name

    @classmethod
    def from_string(cls,string):

        return cls(string)
s1 = Student.from_string("Anamika")
print(s1.name)
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    @classmethod
    def details(cls,data):
        name,age = data.split( "-")
        return cls(name,int(age))
s1 = Student.details("Anamika-18")
print(s1.name)
print(s1.age)
