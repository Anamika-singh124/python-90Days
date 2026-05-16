for i in range (1,4):
    print(i)
else:
    print("Loop completed")
for i in range(1,6):
    if i ==3:
        print(i)
else:
    print("completed")
i = 1
while i <= 3:
    print(i)
    i +=1
else:
    print("dono")
nums = [1,2,3,4]
for i in nums:
    if i == 5:
        print("found")
        break 
else:
    print("not found")
try:
    num = int(input("enter number:"))
    print(num)
except:
    print("invalid input")
try:
    print(10/2)
except:
    print("Error")
else:
     print("no error")
try:
    print(10/2)
except:
    print("error")
finally:
    print("always runs")
age = 18
if age >= 18:
    print("adult")
else:
    print("minor")
num = 5 
result = "even" if num%2 == 0 else "odd"
print(result)
