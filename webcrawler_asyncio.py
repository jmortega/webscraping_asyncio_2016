import asyncio
import random
import time
import requests
import aiosocks
import aiohttp
import re
import bs4

#proxy
from aiosocks.connector import (proxy_connector,
                                SocksConnector, HttpProxyAddr, HttpProxyAuth)


async def get_url_proxy(url):
    
    time_init = time.clock()
    
    conn = proxy_connector(HttpProxyAddr('http://ip_proxy:port_proxy'),None)
    
    try:
        print("Connecting with",url)
        with aiohttp.ClientSession(connector=conn) as session:
            async with session.get(url) as resp:
                if resp.status == 200:
                    
                    time_execution = str(time.clock() - time_init)
                                            
                    print('Done: URL {} took {}s to get!'.format(url, time_execution))
                    
                    return(await resp.text(),url)
                    
                             
    except aiohttp.ProxyConnectionError as e:
        print(e)
    # connection problem
    except aiosocks.SocksError as e:
        print(e)

#regular expression for extract links
html_link_regex = \
           re.compile('<a\s(?:.*?\s)*?href=[\'"](.*?)[\'"].*?>')  


async def get_url(url):
    
    time_init = time.clock()
    
    try:
        print("Connecting with",url)
        with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                if resp.status == 200:
                    
                    time_execution = str(time.clock() - time_init)
                                            
                    print('Done: URL {} took {}s to get!'.format(url, time_execution))
                    
                    return(await resp.text(),url)
                    
                             
    except aiohttp.ProxyConnectionError as e:
        print(e)
    # connection problem
    except aiosocks.SocksError as e:
        print(e)
        

#extract links with BeautifulSoup
def get_links_bs4(page):
    soup = bs4.BeautifulSoup(page,'html.parser')
    links = soup.find_all('a')
    return links

@asyncio.coroutine
def process_as_results_come_in():
    
    coroutines = [get_url(url) for url in ['http://www.python.org', 
                                                 'http://www.google.com', 
                                                 'http://www.github.com']]
    for coroutine in asyncio.as_completed(coroutines):
        result,url = yield from coroutine
        links = get_links_bs4(result)
        for link in links:
            print(link['href'])


@asyncio.coroutine
def process_once_everything_ready():
    coroutines = [get_url(url) for url in ['http://www.python.org',
                                                 'http://www.google.com',
                                                 'http://www.github.com']]
    results = yield from asyncio.gather(*coroutines)
    for result in results:
        links = html_link_regex.findall(result[0])
        for link in links:
            print(result[1]+" "+link)

@asyncio.coroutine
def process_as_futures():
    tasks = [asyncio.ensure_future(get_url(url)) for url in ['http://www.python.org',
                                                                   'http://www.google.com',
                                                                   'http://www.github.com']]
    results=yield from asyncio.gather(*tasks)
    for result in results:
        links = html_link_regex.findall(result[0])
        for link in links:
            print(result[1]+" "+link)
    
def main():
    
    loop = asyncio.get_event_loop()

    time_init = time.clock()  
    
    #loop.run_until_complete(process_as_results_come_in())
    loop.run_until_complete(process_once_everything_ready())
    #loop.run_until_complete(process_as_futures())
    
    time_execution = str(time.clock() - time_init)
                 
    #print('End process_as_results_come_in:',time_execution)      
    print('End process_once_everything_ready:',time_execution)  
    #print('End process_as_futures:',time_execution)
	
if __name__ == '__main__':
    main()
