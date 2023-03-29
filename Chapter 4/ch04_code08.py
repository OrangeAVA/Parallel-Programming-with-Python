async def main():
    task1 = asyncio.create_task(coroutine(10,"A"))
    task2 = asyncio.create_task(coroutine(4,"B"))
    task3 = asyncio.create_task(coroutine(2,"C"))
    r1 = await task1
    r2 = await task2
    r3 = await task3
    results = [ r1, r2, r3]
    print("The results are: %s" %results)
  
asyncio.run(main())

