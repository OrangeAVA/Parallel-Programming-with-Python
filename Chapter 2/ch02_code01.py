import threading
import time

def function(i):
  print ("start Thread %i\n" %i)
  time.sleep(2)
  print ("end Thread %i\n" %i)
  return

t1 = threading.Thread(target=function , args=(1,))
t2 = threading.Thread(target=function , args=(2,))
t3 = threading.Thread(target=function , args=(3,))
t4 = threading.Thread(target=function , args=(4,))
t5 = threading.Thread(target=function , args=(5,))
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
print("END Program")
