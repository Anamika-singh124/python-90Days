apple_price = 210
budget = 200 
if apple_price <= budget:
    print("Alexa, add 1kg apples to cart")
else:
    print("alexa,do not add apples")
num = 10
if num > 0:
    if num % 2 == 0:
        print("positive even")
num = 0
if num > 0:
    print("positive")
elif num < 0:
    print("negative")
else:
    print("zero")
num = 0
if num > 0:
    print("positive")
elif num == 0:
    print("zero")
else:
    print("negative")
num = 15
if num > 0:
    if num <= 10:
      print("number is zero")
if num > 0:
    if num <= 10:
      print("number is between 1-10")
    elif num > 10 and num <= 20:
        print("number is between 11-20 ")
    else:
        print("number is greater than 20")
elif num == 0:
    print("number is zero")
else:
    print("number is negative")