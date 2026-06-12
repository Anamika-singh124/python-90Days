import asyncio
async def task1():
    print("Task 1 stared")
    await asyncio.sleep(2)
    print("task 1 finished")

async def task2():
    print("Task 2 stared")
    await asyncio.sleep(1)
    print("task 2 Finished")

async def main():
    await asyncio.gather(task1(),task2())

asyncio.run(main())

import asyncio
async def greet():
    print("Hello")
    await(asyncio.sleep(2))
    print("World")

asyncio.run(greet())