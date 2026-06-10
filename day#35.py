from functools import lru_cache 

@lru_cache(maxsize=None)
def factorial(n):
    if n ==0:
        return 1
    return n * factorial(n-1)

print(factorial(5))
print(factorial(5))  #Cached result use hoga

print(factorial.cache_info())

from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)
print(fib(40))

