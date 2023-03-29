import multiprocessing
import time

def function(i):
  print ("start Process %i" %i)
  time.sleep(2)
  print ("end Process %i" %i)
  return

if __name__ == '__main__':
  processes = []
  n_procs = 5

  for i in range(n_procs):
    p = multiprocessing.Process(target=function, args=(i,))
    processes.append(p)
    p.start()

  for i in range(n_procs):
    processes[i].join()

  print("END Program")

