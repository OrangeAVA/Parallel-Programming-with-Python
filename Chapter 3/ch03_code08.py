from multiprocessing import Process, Pipe
import time
import random

class Consumer(Process):
  def __init__(self, count, conn):
    Process.__init__(self)
    self.count = count
    self.conn = conn
  
  def run(self):
    for i in range(self.count):
      local = self.conn.recv()
      time.sleep(2)
      print("consumer has used this: %s" %local)

class Producer(Process):
  def __init__(self, count, conn):
    Process.__init__(self)
    self.count = count
    self.conn = conn

  def request(self):
    time.sleep(1)
    return random.randint(0,100)
 
  def run(self):
    for i in range(self.count):
      local = self.request()
      self.conn.send(local)
      print("producer has loaded this: %s" %local)

if __name__ == '__main__':
  recver, sender = Pipe()
  count = 5
  p1 = Producer(count, sender)
  p2 = Consumer(count, recver)
  p1.start()
  p2.start()
  p1.join()
  p2.join()
  recver.close()
  sender.close()

