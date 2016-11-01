import time
import sys
import asyncio


HOST = '127.0.0.1'
PORT = 5566


start_time = time.time()


def printer(start_time, *args, **kwargs):
    '''Simple function to print a message prefixed with the
    time relative to the given start_time'''
    print('%.1f' % (time.time() - start_time), *args, **kwargs)


async def handle_connection(reader, writer):
    client_address = writer.get_extra_info('peername')
    printer(start_time, 'Client connected', client_address)

    # Send over the server start time to get consistent
    # timestamps
    writer.write(b'%.2f\n' % start_time)
    await writer.drain()

    linea=await reader.readline()
    aux=str(linea.decode('utf-8')).split("/")
    repetitions = int(aux[0])
    client_message = str(aux[1])
    printer(start_time, 'Started sending to', client_address)

    for i in range(repetitions):
        message = 'client: %r, %d %s\n' % (client_address, i,client_message)
        printer(start_time, message, end='')
        writer.write(message.encode())
        await writer.drain()

    printer(start_time, 'Finished sending to', client_address)
    writer.close()


async def create_connection(repetitions,message):
    reader, writer = await asyncio.open_connection(
        host=HOST, port=PORT)

    start_time = float((await reader.readline()))

    print('Sended message '+message)
    writer.write(repetitions.encode()+ str("/"+message).encode() + b'\n')
    await writer.drain()

    async for line in reader:
        # Sleeping a little to emulate processing time and make
        # it easier to add more simultaneous clients
        await asyncio.sleep(1)

        printer(start_time, 'Got line: ', line.decode(),
                end='')

    writer.close()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    if sys.argv[1] == 'server':
        server = asyncio.start_server(
            handle_connection,
            host=HOST,
            port=PORT,
        )
        print(server)
        running_server = loop.run_until_complete(server)

        try:
            result = loop.call_later(25, loop.stop)
            loop.run_forever()
        except KeyboardInterrupt:
            sys.exit(1)
            pass

        running_server.close()
        loop.run_until_complete(running_server.wait_closed())
    elif sys.argv[1] == 'client':
        loop.run_until_complete(create_connection(sys.argv[2],sys.argv[3]))

    loop.close()
