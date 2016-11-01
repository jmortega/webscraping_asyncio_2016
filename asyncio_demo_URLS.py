#!/usr/local/bin/python3.5
import asyncio
import aiohttp

async def print_content(url):
    print(url)
    content= await get_content(url)
    
async def get_content(url):
    print(url)
    response= await aiohttp.get(url)
    print(response)
    return (await response.text())

async def print_lot_of_contents(urls):
    tasks=[asyncio.ensure_future(print_content(url))
          for url in urls
          ]
    await asyncio.wait(tasks)
                    
if __name__ == '__main__':
    loop=asyncio.get_event_loop()
    content=loop.run_until_complete(get_content("http://www.python.org"))
    print(content)
    content=loop.run_until_complete(print_lot_of_contents(["http://www.python.org","http://www.python.org"]))
    