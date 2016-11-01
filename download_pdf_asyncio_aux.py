import asyncio
import itertools
import aiohttp
import time
import os

async def download(url, parts):
    async def get_partial_content(u, i, start, end):
        async with aiohttp.get(
                u, headers={"Range": "bytes={}-{}".format(start, end - 1 if end else "")}) as _resp:
            return i, await _resp.read()

    async with aiohttp.head(url) as resp:
        size = int(resp.headers["Content-Length"])

    ranges = list(range(0, size, size // parts))

    res, _ = await asyncio.wait(
        [get_partial_content(url, i, start, end) for i, (start, end) in
         enumerate(itertools.zip_longest(ranges, ranges[1:], fillvalue=""))])

    sorted_result = sorted(task.result() for task in res)
    return b"".join(data for _, data in sorted_result)


if __name__ == '__main__':
    image_url = "http://docs.python.org.ar/tutorial/pdfs/TutorialPython3.pdf"
    
    loop = asyncio.get_event_loop()
    t1 = time.time()
    bs = loop.run_until_complete(download(image_url, 16))

    filename = os.path.basename(image_url)

        
    with open(filename, 'wb') as file_handle:
        file_handle.write(bs)
    
    print('Finished downloading {filename}'.format(filename=filename))
        
    print(time.time() - t1, 'seconds passed')