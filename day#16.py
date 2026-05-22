x = 10
def test():
    x = 50
test()
print(x)
x = 10
def test():
    global x
    x = 50
test()
print(x)
name = "Anamika"
def change():
    global name
    name = "python girl"
change()
print(name)
count = 1
def update ():
    global count
    count = count + 1
update()
print(count)
file = open ("test.txt","w")
file.write("hello python")
file.close()
file = open("test.txt","a")
file.close()
file = open("test.txt","a")
file.write("New Line")
file. close()
with open("test.txt","r") as file:
    print(file.read())
file = open("test.txt","r")
print(file.readlines())
file.close
file = open("demo.txt","w")
date = ["Apple\n","mango\n","banana\n"]
file.writelines(date)
file.close()
