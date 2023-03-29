import threading
import time
  
def thread(num,t):
  print("Thread %s started" %num)
  time.sleep(t)
  print("Thread %s ended" %num)
  
t1 = threading.Thread(target=thread, args=(1,10,))
t2 = threading.Thread(target=thread, args=(2,1,))
t3 = threading.Thread(target=thread, args=(3,10,))
t4 = threading.Thread(target=thread, args=(4,4,))
t1.start()
t2.start()
t3.start()
t4.start()
t1.join()
t2.join()
t3.join()
t4.join()
print("Program ended") 
 
