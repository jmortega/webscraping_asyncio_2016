#!/usr/local/bin/python3.5
import asyncio
from aiohttp import ClientSession

async def fetch(url, session):
    async with session.get(url) as response:
		# async operation must be preceded by await 
        return await response.read()
		
def print_responses(result):
    print(result)
	
async def execute(loop):
    url = "http://www.python.org/{}"
    tasks = []
	sites = ['about','downloads','doc','community','blog','events']
    # Fetch all responses within one Client session,
    # keep connection alive for all requests.
    async with ClientSession() as session:
        for site in sites:
            task = asyncio.ensure_future(fetch(url.format(site), session))
            tasks.append(task)
		# async operation must be preceded by await 
        responses = await asyncio.gather(*tasks)
        # you now have all response bodies in this variable
        print(responses)
		
loop = asyncio.get_event_loop()
future = asyncio.ensure_future(execute(loop))
loop.run_until_complete(future)