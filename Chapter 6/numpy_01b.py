import numpy as np
import time

n = 8
a = np.random.randint(10, size=(n*n))
b = np.random.randint(10, size=(n*n))
c = np.zeros((n*n), dtype=np.float32)

a = a.astype(np.float32)
b = b.astype(np.float32)

def matmul(n, A, B, C):
    # Iterate over the rows of A.
    for i in range(n):
        # Iterate over the columns of B
        for j in range(n):
            tmp = 0.0
            # Iterate over the rows of B.
            for k in range(n):
                tmp += A[i * n + k] * B[k * n + j]
            C[i * n + j] = tmp

t1 = time.perf_counter()
matmul(n, a, b, c)
t2 = time.perf_counter()
elapsed_time = t2 - t1
print("Elapsed time %s" %elapsed_time)

