marks = [90,85,78,95]
print(marks[0])
print(marks[1])
lst1 = [1,2,23,5,4,6]
lst2 = ["Red","green","blue"]
print(lst1)
print(lst2)
details = ["abbijeet",18,"FYBSCIT",9.8]
print(details)
colors = ["Red","Blue","Pink","yellow"]
print([3])
print([2])
print(marks[-1])
numbers = [1,2,3,4,5]
print(numbers[1:4])
marks = [90,83,78]
marks[1] = 100
print(marks)
fruits = ["apple","banana"]
fruits.append("mango")
print(fruits)
numbers = [1,2,3,4]
for i in numbers:
    print(i)
students = ["Anamika","Nisha","Sonam","priyanshi"]
for i in students:
    print(i)
name = ["golu","suraj","yash","aman","harsh"]
if "yash" in name:
    print("yash is present.")
else:
    print("yash is absent.")
animals = ["cat","dog","ox","goat","donkey","fox","dog"]
print(animals[3:4])
print(animals[-7:-3])
print(animals[0:8:2])
print(animals[4:])
print(animals[-4:])
print(animals[:6])
print(animals[::2])
print(animals[-8:-1:2])
print(animals[1:8:3])
numbers = []
for i in range(1,6):
    numbers.append(i)
print(numbers)
numbers =[i for i in range(1,6)]
print(numbers)
square = [i*i for i in range(1,6)]
print(square)
even = [i for i in range(1,11)if i%2 ==0]
print(even)
odd = [i for i in range(1,11)if i%2!=0]
print(odd)
names = ["anamika","riya","pooja"]
upper = [name.upper()for name in names]
print(upper)
num = [4,2,3,4,5,6,7,4,9,7]
num.sort()
print(num)
colors1 = ["voilet","indogo","blue","green",]
colors2 = ["yellow","orange","red"]
print(colors1 + colors2)
num.sort(reverse=True)
print(num)
nums = [1,2,3,4,5]
print(nums.count(2))
a = [1,2,3]
b = a.copy()
print(b)
a = [1,2]
b = [3,4]
a.extend(b)
print(a)
a = [1,2]
b = [ 3,4]
a.append(b)
print(a)
