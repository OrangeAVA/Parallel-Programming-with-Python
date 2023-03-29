import numpy as np

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

matmul(n, a, b, c)
print("Matrix A")
print(a.reshape(n,n))
print("Matrix B")
print(b.reshape(n,n))
print("Matrix A*B")
print(c.reshape(n,n))

