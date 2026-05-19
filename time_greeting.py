import time 
hour = int(time.strftime('%H'))
print("current hour:",hour)
if hour  < 12:
    print("Good morning")
elif  hour < 17:
    print("Good afternoon")
else:
    print("Good evening")
