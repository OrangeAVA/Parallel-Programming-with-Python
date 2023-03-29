import asyncio
import random

async def producer(name, queue):
    n = random.randint(0, 10)
    await asyncio.sleep(n)
    await queue.put(n)
    print("Producer %s adds %s to the queue" %(name,n))
    
async def consumer(name, queue):
    while True:
        n = await queue.get()
        await asyncio.sleep(n)
        print("Consumer %s receives %s from the queue" %(name,n))
        queue.task_done()

async def main(nproducers, nconsumers):
    q = asyncio.Queue()
    producers = [asyncio.create_task(producer(n, q)) for n in range(nproducers)]
    consumers = [asyncio.create_task(consumer(n, q)) for n in range(nconsumers)]
    
    await asyncio.gather(*producers)
    await q.join()  
    for c in consumers:
        c.cancel()


asyncio.run(main(4,2))

