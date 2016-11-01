import asyncio
print('Starting')
loop=asyncio.get_event_loop()

async def something(name):
    for i in range(10):
        print(name,i)
        await asyncio.sleep(1)
        
loop.run_until_complete(something('Task'))