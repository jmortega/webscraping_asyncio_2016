#!/usr/local/bin/python3.5
import requests
import asyncio
import aitohttp

URLS=['http://www.python.org','http://www.python.org']

async def fetch(url):
    return await loop.run_in_executor(None,requests.get,url)

#methods equivalents

async def fetch2(url):
    with aitohttp.ClientSession() as session:
	async with session.get(url) as response:
	    return await response.read()
	
try:
    loop=asyncio.get_event_loop()
    tasks=[fetch(url) for url in  URLS]
    responses=loop.run_until_complete(asyncio.gather(*tasks))
    print(responses)
finally:
    loop.close()