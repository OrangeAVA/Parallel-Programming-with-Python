import threading
import time

shared = 0
lock = threading.Lock()

def funcA():
  global shared
  for i in range(10):
    time.sleep(1)
    shared += 10
    print("Thread A wrote: %s, %i" %(shared,i))
    lock.acquire()

def funcB():
  global shared
  lock.acquire()
  for i in range(10):
    time.sleep(1)
    shared -= 10
    print("Thread B wrote: %s, %i" %(shared,i))
    lock.release()
    
t1 = threading.Thread(target = funcA)
t2 = threading.Thread(target = funcB)
t1.start()
t2.start()
t1.join()
t2.join()
