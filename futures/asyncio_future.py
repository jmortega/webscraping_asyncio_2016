import asyncio
import time

#FACTORIAL(N)
@asyncio.coroutine
def factorial(future,number):
    count = 1
    for i in range(2, number+1):
        count *= i
        yield from asyncio.sleep(1)
    future.set_result("factorial("+str(number)+ ")="+str(count))

#got_result is a function that prints the final result of the future: 
def got_result(future):
    print(future.result())

    
if __name__ == "__main__":
    #we define the objects' future to associate the coroutines:
    future = asyncio.Future()
    future1 = asyncio.Future()
    future2 = asyncio.Future()
    future3 = asyncio.Future()
    
    #we add a callback that is to be run when the future gets executed
    future.add_done_callback(got_result)
    future1.add_done_callback(got_result)
    future2.add_done_callback(got_result)
    future3.add_done_callback(got_result)     

    t1 = time.time()
    
    #While defining the tasks, we pass the object future as 
    #an argument of factorial coroutine:
    tasks = [
        factorial(future,10),
        factorial(future1,5),
        factorial(future2,2),
        factorial(future3,1)]
    
           
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    
    print(time.time() - t1, "seconds passed")
    
    loop.close()

