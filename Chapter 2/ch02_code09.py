import threading
import time

shared_data = 0

def funcA():
  global shared_data
  for i in range(10):
    local = shared_data
    local += 10
    time.sleep(1)
    shared_data = local
    print("Thread A wrote: %s" %shared_data)

def funcB():
  global shared_data
  for i in range(10):
    local = shared_data
    local -= 10
    time.sleep(1)
    shared_data = local
    print("Thread B wrote: %s" %shared_data)

t1 = threading.Thread(target = funcA)
t2 = threading.Thread(target = funcB)
t1.start()
t2.start()
t1.join()
t2.join()
