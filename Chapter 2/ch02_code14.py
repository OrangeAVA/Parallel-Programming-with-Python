import threading
import time

shared = 0
rlock = threading.RLock()

def func(name, t):
  global shared
  for i in range(3):
    rlock.acquire()
    local = shared
    time.sleep(t)
    for j in range(2):
      rlock.acquire()
      local += 1
      time.sleep(2)
      shared = local
      print("Thread %s-%s wrote: %s" %(name, j, shared))
      rlock.release()  
    shared = local + 1
    print("Thread %s wrote: %s" %(name, shared))
    rlock.release()

t1 = threading.Thread(target = func,args=('A',2,))
t2 = threading.Thread(target = func,args=('B',10,))
t3 = threading.Thread(target = func,args=('C',1,))
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()

