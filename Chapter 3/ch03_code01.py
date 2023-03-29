import multiprocessing
import time

def function(i):
  print ("start Process %i" %i)
  time.sleep(2)
  print ("end Process %i" %i)
  return

if __name__ == '__main__':
  p1 = multiprocessing.Process(target=function, args=(1,))
  p2 = multiprocessing.Process(target=function, args=(2,))
  p3 = multiprocessing.Process(target=function, args=(3,))
  p4 = multiprocessing.Process(target=function, args=(4,))
  p5 = multiprocessing.Process(target=function, args=(5,))
  p1.start()
  p2.start()
  p3.start()
  p4.start()
  p5.start()
  p1.join()
  p2.join()
  p3.join()
  p4.join()
  p5.join()
  print("END Program")

