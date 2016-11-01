import asyncio
import itertools
import aiohttp
import time

async def download(url, parts):
    async def get_partial_content(u, i, start, end):
        print(i, start, end)
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
    image_url = "http://blog.hunabsys.com/wp-content/uploads/2016/05/a1.jpg"
    
    loop = asyncio.get_event_loop()
    t1 = time.time()
    bs = loop.run_until_complete(download(image_url, 16))

    with open("test_for_asyncio.jpeg", "wb") as fi:
        fi.write(bs)
        
    print(time.time() - t1, 'seconds passed')