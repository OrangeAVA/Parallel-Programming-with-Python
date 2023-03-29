import asyncio

async def main():
  print('Starting...')
  await asyncio.sleep(10)
  print('...Ending')
  
#asyncio.run(main())
loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(main())
finally:
    loop.close()

