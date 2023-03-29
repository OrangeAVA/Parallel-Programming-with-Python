import asyncio

async def get_result(result):
    await asyncio.sleep(5)
    result = '...an awaited result'

async def main():
    my_result = ' '
    task1 = asyncio.create_task(get_result(my_result))
    await task1
  
    print("I'm waiting for ...")
    print(my_result)

asyncio.run(main())

