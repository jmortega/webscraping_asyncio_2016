import asyncio
import time

@asyncio.coroutine
def factorial(number):
    count = 1
    for i in range(2, number+1):
        print("Asyncio.Task: Compute factorial(%s)" % (i))
        count *= i
        yield from asyncio.sleep(1)
        
    print("Asyncio.Task - factorial(%s) = %s" % (number, count))

@asyncio.coroutine
def fibonacci(number):
    a, b = 0, 1
    for i in range(number):
        print("Asyncio.Task: Compute fibonacci (%s)" % (i))
        yield from asyncio.sleep(1)
        a, b = b, a + b
    print("Asyncio.Task - fibonacci(%s) = %s" % (number, a))


if __name__ == "__main__":
    t1 = time.time()
    loop = asyncio.get_event_loop()
    task1=loop.create_task(factorial(10))
    task2=loop.create_task(factorial(5))
    task3=loop.create_task(factorial(2))
    task4=loop.create_task(factorial(1))
    loop.run_until_complete(asyncio.gather(task1,task2,task3,task4))
    print(time.time() - t1, "seconds passed")
    loop.close()
