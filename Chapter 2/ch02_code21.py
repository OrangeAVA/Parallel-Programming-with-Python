from threading import Thread, Event
import time
import random

event = Event()
shared = 1
count = 5

class Consumer(Thread):
  def __init__(self, count):
    Thread.__init__(self)
    global event
    self.count = count
  
  def run(self):
    global shared
    for i in range(self.count):
      event.wait()
      print("consumer has used this: %s" %shared)
      shared = 0
      event.clear()

class Producer(Thread):
  def __init__(self, count):
    Thread.__init__(self)
    self.count = count
    global event

  def request(self):
    time.sleep(1)
    return random.randint(0,100)
 
  def run(self):
    global shared
    for i in range(self.count):
      shared = self.request()
      print("producer has loaded this: %s" %shared)
      event.set()

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

