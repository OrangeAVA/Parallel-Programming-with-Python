import multiprocessing
import os
import time

def function():
  pid = os.getpid()
  print ("start Process %s" %pid)
  time.sleep(2)
  print ("end Process %s" %pid)
  return

if __name__ == '__main__':
  processes = []
  n_procs = 5

  for i in range(n_procs):
    p = multiprocessing.Process(target=function)
    processes.append(p)
    p.start()

  for i in range(n_procs):
    processes[i].join()

  print("END Program")

