import asyncio
import aiohttp

# ----------------------------------------------------------------------
@asyncio.coroutine
def print_page(url):
    response = yield from aiohttp.request('GET', url)
    body = yield from response.read()

    print(body)


# ----------------------------------------------------------------------
def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(print_page('http://navajanegra.com'))
    loop.close()


if __name__ == '__main__':
    main()