import asyncio

async def main():
    print('Awaiting for ...')
    await asyncio.sleep(1)
    print('... AsyncIO!')

asyncio.run(main())
