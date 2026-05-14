fruits = {"apple","banana","mango"}
print(fruits)
nums = {1,2,3,2,1,4}
print(nums)
a = set()
print(type(a))
colours = {"red","blue","green"}
for i in colours:
    print(i)
a = {1,2,3}
b = {3,4,5}
print(a.union(b))
a = {1,2}
b = {3,4}
a.update(b)
print(a)
s = {1,2}
s.add(3)
print(s)
s = {1,2,3}
s.remove(2)
print(s)
s = {1,2,3}
s.discard(5)
print(s)
s = {"a","b","c"}
s.pop()
print(s)
s = {1,2,3}
s.clear()
s.clear()
print(s)
a = {1,2,3}
b = a.copy()
print(b)
a = {1,2,3}
b = {2,3,4}
print(a.intersection(b))
a = {1,2,3}
b = {2,3,4}
print(a.difference(b))
a = {1,2,3}
b = {2,3,4}
print(a.symmetric_difference(b))
