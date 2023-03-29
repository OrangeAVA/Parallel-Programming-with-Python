asyncio.sleep(). 
import asyncio

async def other(id,t):
  await asyncio.sleep(t)
  print("I am a coroutine %s" %id)

async def main():
    task1 = asyncio.create_task(other(1,10))
    task2 = asyncio.create_task(other(2,4))
    task3 = asyncio.create_task(other(3,1))
    await task1
    await task2
    await task3

asyncio.run(main())

