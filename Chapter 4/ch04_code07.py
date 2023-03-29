
import asyncio
async def coroutine(t,id):
   await asyncio.sleep(t)
   print("I am the coroutine %s" %id)
   return t+2
  
async def main():
    results = await asyncio.gather(
        coroutine(10,"A"),
        coroutine(4,"B"),
        coroutine(2,"C"),
    )
    print("The results are: %s" %results)

asyncio.run(main())

