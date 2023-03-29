import numpy as np
from numba import cuda
import time
import math

@cuda.jit
def matmul(A, B, C):

    i, j = cuda.grid(2)
    if i < C.shape[0] and j < C.shape[1]:
        tmp = 0.
        for k in range(A.shape[1]):
            tmp += A[i, k] * B[k, j]
        C[i, j] = tmp

print("Matrix Size: ")
n = input()
print("\n")
A_host = np.random.random(n*n).reshape(n,n)
B_host = np.random.random(n*n).reshape(n,n)
C_host = np.zeros((n,n))

stream = cuda.stream()
A_dev = cuda.to_device(A_host, stream=stream)
B_dev = cuda.to_device(B_host, stream=stream)
C_dev = cuda.to_device(C_host, stream=stream)

threadsperblock = (128,128)
blockspergrid_x = math.ceil(A_host.shape[0] / threadsperblock[0])
blockspergrid_y = math.ceil(A_host.shape[1] / threadsperblock[1])
blockspergrid = (blockspergrid_x, blockspergrid_y)
matmul[threadsperblock, blockspergrid](A_dev, B_dev, C_dev)

t1 = time.perf_counter()
C_host = C_dev.copy_to_host(stream=stream)
t2 = time.perf_counter()
elapsed_time = t2 - t1
print("Elapsed time %s" %elapsed_time)

