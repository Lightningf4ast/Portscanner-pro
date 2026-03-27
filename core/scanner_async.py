import asyncio

async def scan_port(ip, port, timeout):
    try:
        conn = asyncio.open_connection(ip, port)
        reader, writer = await asyncio.wait_for(conn, timeout=timeout)

        writer.close()
        await writer.wait_closed()

        return port
    except:
        return None


async def scan_range(ip, start, end, timeout):
    tasks = []

    for port in range(start, end + 1):
        tasks.append(scan_port(ip, port, timeout))

    results = await asyncio.gather(*tasks)

    return [p for p in results if p]
