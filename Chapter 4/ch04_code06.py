import asyncio

async def other(t):
  await asyncio.sleep(t)
  id =  asyncio.current_task().get_name()
  print("I am a coroutine %s" %id)

async def main():
    task1 = asyncio.create_task(other(10),name="1")
    task2 = asyncio.create_task(other(4),name="2")
    task3 = asyncio.create_task(other(3),name="3")
    await task1
    await task2
    await task3

asyncio.run(main())   

