from threading import Thread, Semaphore
import time
import random

semaphore = Semaphore(1)
shared = 1

class Consumer(Thread):
  def __init__(self):
    Thread.__init__(self)
    global semaphore

  def run(self):
    global shared
    with semaphore: 
      print("consumer has used this: %s" %shared)
      shared = 0

class Producer(Thread):
  def __init__(self):
    Thread.__init__(self)
    global semaphore

  def request(self):
    time.sleep(1)
    return random.randint(0,100)

  def run(self):
    global shared
    with semaphore:
      shared = self.request()
      print("producer has loaded this: %s" %shared)
      
t1 = Producer()
t2 = Consumer()
t1.start()
t2.start()
t1.join()
t2.join()

