from threading import Thread, Semaphore
import time
import random

semaphore = Semaphore(1)
shared = 1
count = 5

class consumer(Thread):
  def __init__(self, count):
    Thread.__init__(self)
    global semaphore
    self.count = count

  def run(self):
    global shared
    for i in range(self.count):
      semaphore.acquire()
      print("consumer has used this: %s" %shared)
      shared = 0
      semaphore.release()

class producer(Thread):
  def __init__(self, count):
    Thread.__init__(self)
    self.count = count
    global semaphore

  def request(self):
    time.sleep(1)
    return random.randint(0,100)

  def run(self):
    global shared
    for i in range(self.count):
      semaphore.acquire()
      shared = self.request()
      print("producer has loaded this: %s" %shared)
      semaphore.release()

t1 = producer(count)
t2 = consumer(count)
t1.start()
t2.start()
t1.join()
t2.join()

