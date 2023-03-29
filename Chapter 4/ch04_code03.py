import asyncio

async def other():
  print("I am a coroutine")

async def main():
    task = asyncio.create_task(other())
    print('Awaiting for ...')
    await asyncio.sleep(1)
    await task
    print('... AsyncIO!')

asyncio.run(main())
