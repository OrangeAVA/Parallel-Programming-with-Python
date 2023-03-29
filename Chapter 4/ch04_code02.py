import asyncio

async def other():
  print("I am a coroutine")

async def main():
    print('Awaiting for ...')
    await asyncio.sleep(1)
    await other()
    print('... AsyncIO!')

asyncio.run(main())

