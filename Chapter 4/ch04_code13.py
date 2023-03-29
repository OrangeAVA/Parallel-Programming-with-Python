import asyncio

async def f(i):
    print('start iteration step %s' %i)
    await asyncio.sleep(1)
    print('end iteration step %s' %i)
    return i

async def main():
  for j in asyncio.as_completed([f(i) for i in range(10)]):
      result = await j
      print('result received: %s' %result)

asyncio.run(main())

