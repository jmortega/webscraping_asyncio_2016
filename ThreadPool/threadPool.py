
import asyncio
from concurrent.futures import ThreadPoolExecutor

async def first_completed(urls):
    print("First completed")
    
def run_in_background(loop):
    asyncio.set_event_loop(loop)
    try:
        loop.run_forever()
    finally:
        print('Finishing...')
        loop.run_until_complete(cancel_all(asyncio.Task.all_tasks(loop=loop)))
        loop.close()
    

loop = asyncio.get_event_loop()
executor = ThreadPoolExecutor(max_workers=2)
background_future=executor.submit(run_in_background,loop)

urls=['http://www.python.org']

f=asyncio.run_coroutine_threadsafe(first_completed(urls),loop)
print('result',f.result())
loop.call_soon_threadsafe(loop.stop)
executor.shutdown(wait=True)