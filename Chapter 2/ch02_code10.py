import threading
import time

shared = 0
lock = threading.Lock()

def funcA():
  global shared
  for i in range(10):
    lock.acquire()
    local = shared
    local += 10
    time.sleep(1)
    shared = local
    print("Thread A wrote: %s" %shared)
    lock.release()

def funcB():
  global shared
  for i in range(10):
    lock.acquire()
    local = shared
    local -= 10
    time.sleep(1)
    shared = local
    print("Thread B wrote: %s" %shared)
    lock.release()
    
t1 = threading.Thread(target = funcA)
t2 = threading.Thread(target = funcB)
t1.start()
t2.start()
t1.join()
t2.join()

