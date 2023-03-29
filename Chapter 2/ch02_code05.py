import concurrent.futures
import time
  
def thread(num,t):
  print("Thread %s started" %num)
  time.sleep(t)
  print("Thread %s ended" %num)
  
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as t:
   t.submit(thread(1,10))
   t.submit(thread(2,1))
   t.submit(thread(3,10))
   t.submit(thread(4,4))

print("Program ended")
