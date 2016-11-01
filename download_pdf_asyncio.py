import asyncio
import os
import urllib.request
import time


async def download_coroutine(url):
    """
    A coroutine to download the specified url
    """
    request = urllib.request.urlopen(url)
    filename = os.path.basename(url)
 
    with open(filename, 'wb') as file_handle:
        while True:
            chunk = request.read(1024)
            if not chunk:
                break
            file_handle.write(chunk)
    msg = 'Finished downloading {filename}'.format(filename=filename)
    return msg
 
async def main(urls):
    coroutines = [download_coroutine(url) for url in urls]
    completed, pending = await asyncio.wait(coroutines)
    for item in completed:
        print(item.result())
 
 
if __name__ == '__main__':
    urls = ["http://docs.python.org.ar/tutorial/pdfs/TutorialPython3.pdf"]
    
    t1 = time.time()
    event_loop = asyncio.get_event_loop()
    try:
        event_loop.run_until_complete(main(urls))
    finally:
        event_loop.close()
    print(time.time() - t1, 'seconds passed')