from multiprocessing import Process

def task1():
    print("Task 1 running")

def task2():
    print("Task 2 running")

p1 = Process(target=task1)
p2 = Process(target=task2)

p1.start()
p2.start()

p1.join()
p2.join()

print("Main Process Finished")

from multiprocessing import process

def show():
    print("Process is running")

p = Process(target=show)
p.start()
p.join()


