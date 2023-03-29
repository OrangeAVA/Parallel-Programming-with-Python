import asyncio

async def other(id,t):
  await asyncio.sleep(t)
  print("I am a coroutine %s" %id)

async def main():
    t1 = time.perf_counter()
    await other(10,1)
    await other(4,2)
    await other(3,3)
    t2 = time.perf_counter()
    elapsed_time = t2 - t1
    print("Elapsed time %s" %elapsed_time)

asyncio.run(main())

