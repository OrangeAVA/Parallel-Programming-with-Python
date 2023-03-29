import multiprocessing
import time

def function(i):
  process = multiprocessing.current_process()
  print ("start Task %i(pid:%s)" %(i,process.pid))
  time.sleep(2)
  print ("end Task %i(pid:%s)" %(i,process.pid))
  return

if __name__ == '__main__':
  pool = multiprocessing.Pool(processes=4)
  print("Processes started: %s" %pool._processes)
  for i in range(12):
    results = pool.apply(function, args=(i,))
  pool.close()

  print("END Program")

