x = 2
match x:
    case 1:
        print("one")
    case 2:
        print("two")
    case 3:
        print ( "three")
    case _:
        print("no match")
day = 7
match day:
    case 1:
        print("monday")
    case 2:
        print("tuesday")
    case _:
        print("invalid day")
for i in range(5):
    print(i)
    for i in range (1,6):
        print(i)
for i in range(1,10,2):
    print(i)
for i in range(5,0,-1):
    print(i)
name = "anamika"
for i in name:
    print(i)
colours = ["red","blue","green"]
for x in colours:
    print(x)
for i in range(1,10):
    print(i)
count = 1
while count  <= 5:
    print(count)
    count = count + 1
count = 5
while count > 0:
    print(count)
    count -= 1
fruit = ["apple","banana","mango"]
x = 1
while x < 5:
    if x == 3:
        break
    print(x)
    x += 1
else:
    print("done")
for i in range (1,6):
    if i ==3:
        break
    print(i)

    print(i)

for i in range (1,6):
    if i ==3:
        continue
    print(i)
x = 1
while x <= 3:
    print(x)
    x += 1
else:
    print("loop finished")
