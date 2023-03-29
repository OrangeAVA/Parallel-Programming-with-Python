import asyncio

async def gen(n):
  for i in range(n):
    await asyncio.sleep(1)
    yield i
async def main():
    async for i in gen(10):
      print(i)

asyncio.run(main())

