from threading import Thread
import time

sequence = ""
COUNT = 5
timeA = 5
timeB = 10

class ThreadA(Thread):
  def __init__(self):
    Thread.__init__(self)
    
  def run(self):
    global sequence
    for i in range(COUNT):
      time.sleep(timeA)
      sequence = "%sA" %sequence
      print("Sequence: %s" %sequence)

class ThreadB(Thread):
  def __init__(self):
    Thread.__init__(self)
    
  def run(self):
    global sequence
    for i in range(COUNT):
      time.sleep(timeB)
      sequence = "%sB" %sequence
      print("Sequence: %s" %sequence)

# the Main program
t1 = ThreadA()
t2 = ThreadB()
t1.start()
t2.start()
t1.join()
t2.join()

