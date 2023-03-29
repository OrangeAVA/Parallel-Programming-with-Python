from threading import Thread
from queue import Queue
import time
import random

queue = Queue()
shared = 1
count = 5

class Consumer(Thread):
  def __init__(self, count):
    Thread.__init__(self)
    self.count = count
  
  def run(self):
    global queue
    for i in range(self.count):
      local = queue.get()
      print("consumer has used this: %s" %local)
      queue.task_done()

class Producer(Thread):
  def __init__(self, count):
    Thread.__init__(self)
    self.count = count

  def request(self):
    time.sleep(1)
    return random.randint(0,100)
 
  def run(self):
    global queue
    for i in range(self.count):
      local = self.request()
      queue.put(local)
      print("producer has loaded this: %s" %local)

t1 = Producer(count)
t2 = Producer(count)
t3 = Consumer(count)
t4 = Consumer(count)
t1.start()
t2.start()
t3.start()
t4.start()
t1.join()
t2.join()
t3.join()
t4.join()

