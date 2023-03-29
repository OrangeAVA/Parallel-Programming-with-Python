import dramatiq
import time
from dramaserver import wait

#a = time.perf_counter()
[wait.send(10,i) for i in range(10)]
print("End Program")
#b = time.perf_counter()
#elapsed_time = b - a
#print("Elapsed time: %s secs" %elapsed_time)