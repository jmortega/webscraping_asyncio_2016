import asyncio
future =asyncio.Future()

print(future.done())
try:
    future.result()
except Exception as e:
    print(e)
    
future.set_result("hello")
print(future.result())