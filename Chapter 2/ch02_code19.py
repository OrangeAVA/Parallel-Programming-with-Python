from threading import Thread, Condition
import time
import random

condition = Condition()
shared = 1
count = 5

class Consumer(Thread):
  def __init__(self, count):
    Thread.__init__(self)
    global condition
    self.count = count
  
  def run(self):
    global shared
    for i in range(self.count):
      condition.acquire()
      if shared == 0:
        condition.wait()
      print("consumer has used this: %s" %shared)
      shared = 0
      condition.notify()
      condition.release()

class Producer(Thread):
  def __init__(self, count):
    Thread.__init__(self)
    self.count = count
    global condition

  def request(self):
    time.sleep(1)
    return random.randint(0,100)
 
  def run(self):
    global shared
    for i in range(self.count):
      condition.acquire()
      shared = self.request()
      print("producer has loaded this: %s" %shared)
      condition.wait()
      if shared == 0:
        condition.notify()
      condition.release()

t1 = Producer(count)
t2 = Consumer(count)
t1.start()
t2.start()
t1.join()
t2.join() 
