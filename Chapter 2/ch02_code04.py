import threading
import time

def function(i):
  print ("start Thread %i" %i)
  time.sleep(2)
  print ("end Thread %i" %i)
  return

n_threads = 5
threads = [ ]
for i in range(n_threads):
  t = threading.Thread(target=function , args=(i,))
  threads.append(t)
  t.start()

for i in range(n_threads):
  threads[i].join()
