#!/usr/local/bin/python3.5
import asyncio
import aiohttp

url = 'http://python.org'

async def request_url2():
    resp = await aiohttp.get(url)
    text = await resp.text()
    return text

@asyncio.coroutine
def get_page():
    resp = yield from aiohttp.request('GET',url)
    text = yield from resp.read()
    return text

@asyncio.coroutine
def request_url():
    resp = yield from aiohttp.get(url)
    text = yield from resp.text()
    return text

loop = asyncio.get_event_loop()
content = loop.run_until_complete(request_url())
print(content)
loop.close()
