import numpy as np
from numba import cuda
import math

@cuda.jit
def matmul(A, B, C):

    i, j = cuda.grid(2)
    if i < C.shape[0] and j < C.shape[1]:
        tmp = 0.
        for k in range(A.shape[1]):
            tmp += A[i, k] * B[k, j]
        C[i, j] = tmp

n = 4
A_host = np.random.random(n*n).reshape(n,n)
B_host = np.random.random(n*n).reshape(n,n)
C_host = np.zeros((n,n))
print("Matrix A: \n %s" %A_host)
print("Matrix B: \n %s" %B_host)

stream = cuda.stream()
A_dev = cuda.to_device(A_host, stream=stream)
B_dev = cuda.to_device(B_host, stream=stream)
C_dev = cuda.to_device(C_host, stream=stream)

threadsperblock = (128,128)
blockspergrid_x = math.ceil(A_host.shape[0] / threadsperblock[0])
blockspergrid_y = math.ceil(A_host.shape[1] / threadsperblock[1])
blockspergrid = (blockspergrid_x, blockspergrid_y)
matmul[threadsperblock, blockspergrid](A_dev, B_dev, C_dev)

C_host = C_dev.copy_to_host(stream=stream)
print("Matrix C: \n %s" %C_host)

