import numpy as np
from numba import cuda

@cuda.jit
def add_one(a):
    tx = cuda.threadIdx.x
    ty = cuda.blockIdx.x
    dim = cuda.blockDim.x

    pos = tx + ty * dim
    if pos < a.size:  
        a[pos] += 1

n = 10
a_host = np.random.random(n)
print("Vector a: %s" %a_host)
a_dev = cuda.to_device(a_host)

threadsperblock = 128
blockspergrid = (a_host.size // threadsperblock) + 1
add_one[threadsperblock, blockspergrid](a_dev)

a_host = a_dev.copy_to_host()
print("New Vector a: %s" %a_host)

