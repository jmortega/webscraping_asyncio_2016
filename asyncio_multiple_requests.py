#!/usr/local/bin/python3.5

import asyncio
import aiohttp
import time

URLS = [
    'http://www.python.org',
    'http://www.pycon.org'
]

@asyncio.coroutine
def request_urls():
    response_tasks = yield from asyncio.wait([aiohttp.get(url) for url in URLS])
    text_tasks = yield from asyncio.wait(
        [task.result().text() for task in response_tasks[0]]
    )
    texts = [task.result() for task in text_tasks[0]]
    return '\n'.join(texts)


loop = asyncio.get_event_loop()
t1 = time.time()
urls = loop.run_until_complete(request_urls())
print(time.time() - t1, 'seconds passed')
print(urls)
loop.close()
