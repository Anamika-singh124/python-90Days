import threading

def task1():
    print("Task 1 running")

def task2():
    print("Task 2 running")

t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

t1.start()
t2.start()

t1.join()
t2.join()

print("Main program finished")

import threading

def show():
    print("Thread is running")

thread = threading.Thread(target=show)
thread.start()
thread.join()

