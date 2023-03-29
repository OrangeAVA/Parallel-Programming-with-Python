
import threading
import time

def function(i):
  print ("start Thread %i" %i)
  time.sleep(2)
  print ("end Thread %i" %i)
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
t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
print("END Program")  
