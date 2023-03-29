import asyncio

async def get_result(future):
    await asyncio.sleep(5)
    future.set_result('...a future result')

async def main():
    my_future = asyncio.Future()
    task1 = asyncio.create_task(get_result(my_future))
    await task1
  
    print("I'm waiting for ...")
    print(await my_future)
    print('Before continuing with my execution')

asyncio.run(main())

