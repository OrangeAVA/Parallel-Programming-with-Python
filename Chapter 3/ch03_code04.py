import multiprocessing
import time

def function(i):
  process = multiprocessing.current_process()
  print ("start Process %i(pid:%s)" %(i,process.pid))
  time.sleep(2)
  print ("end Process %i(pid:%s)" %(i,process.pid))
  return

if __name__ == '__main__':
  pool = multiprocessing.Pool()
  print("Processes started: %s" %pool._processes)
  for i in range(pool._processes):
    results = pool.apply(function, args=(i,))
  pool.close()

  print("END Program")

