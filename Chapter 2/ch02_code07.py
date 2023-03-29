import threading
import time

sequence = ""
COUNT = 5
timeA = 5
timeB = 10

def addA():
  global sequence
  for i in range(COUNT):
    time.sleep(timeA)
    sequence = "%sA" %sequence
    print("Sequence: %s" %sequence)

def addB():
  global sequence
  for i in range(COUNT):
    time.sleep(timeB)
    sequence = "%sB" %sequence
    print("Sequence: %s" %sequence)

# the Main program
t1 = threading.Thread(target = addA)
t2 = threading.Thread(target = addB)
t1.start()
t2.start()
t1.join()
t2.join()

