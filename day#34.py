def count():
    yield 1
    yield 2
    yield 3
g = count()
print(next(g))
print(next(g))
print(next(g))

def numbers():
    for i in range(1000000):
        yield i

def greeting():
    yield "Hello"
    yield "hi"
    yield "welcome"

g = greeting()

print(next(g))
print(next(g))
print(next(g))


def test():
    yield 10
    yield 20

g = test()

print(next(g))
print(next(g))

names = (name.upper() for name in[ "anamika","anshika","yash"])
for n in names:
    print(n)
nums = [x*x for x in range(5)]       
print(nums)

