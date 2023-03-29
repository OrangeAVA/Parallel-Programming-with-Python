import numpy as np
from numba import cuda
#import time

@cuda.jit
def add_one(a):
    pos = cuda.grid(1)
    if pos < a.size:  
        a[pos] += 1

n = 10
a_host = np.random.random(n)
print("Vector a: %s" %a_host)
a_dev = cuda.to_device(a_host)

threadsperblock = 128
blockspergrid = (a_host.size // threadsperblock) + 1

#t1 = time.perf_counter()
add_one[threadsperblock, blockspergrid](a_dev)

a_host = a_dev.copy_to_host()
print("New Vector a: %s" %a_host)

#t2 = time.perf_counter()
#elapsed_time = t2 - t1
#print("Elapsed time %s" %elapsed_time)