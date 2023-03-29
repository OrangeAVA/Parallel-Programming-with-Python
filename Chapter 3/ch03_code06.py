from multiprocessing import Process
import time
import random

class ChildProcess(Process):
  def __init__(self, count):
    Process.__init__(self)
    self.count = count
  
  def run(self):
    print ("start Process %s" %self.count)
    time.sleep(2)
    print ("end Process %s" %self.count)

if __name__ == '__main__':
  processes = []
  n_procs = 5

  for i in range(n_procs):
    p = ChildProcess(i)
    processes.append(p)
    p.start()

  for i in range(n_procs):
    processes[i].join()

