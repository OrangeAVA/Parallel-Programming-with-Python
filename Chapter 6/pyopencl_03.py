import pyopencl as cl
import numpy as np

import os
os.environ['PYOPENCL_CTX'] = '0'

n = 8

a = np.random.randint(10, size=(n*n))
b = np.random.randint(10, size=(n*n))
c = np.zeros((n*n), dtype=np.float32)

a = a.astype(np.float32)
b = b.astype(np.float32)

ctx = cl.create_some_context()
queue = cl.CommandQueue(ctx)

mf = cl.mem_flags
a_buf = cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=a)
b_buf = cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=b)
c_buf = cl.Buffer(ctx, mf.WRITE_ONLY, c.nbytes)

prg = cl.Program(ctx, """
    __kernel void multiply(ushort n,
    ushort m, ushort p, __global float *a,
    __global float *b, __global float *c)
    {
      int gid = get_global_id(0);
      c[gid] = 0.0f;
      int rowC = gid/p;
      int colC = gid%p;
      __global float *pA = &a[rowC*m];
      __global float *pB = &b[colC];
      for(int k=0; k<m; k++)
      {
         pB = &b[colC+k*p];
         c[gid] += (*(pA++))*(*pB);
      }
    }
    """).build()

prg.multiply(queue, c.shape, None,
             np.uint16(n), np.uint16(n), np.uint16(n),
             a_buf, b_buf, c_buf)

cl.enqueue_copy(queue, c, c_buf)

print("Matrix A")
print(a.reshape(n,n))
print("Matrix B")
print(b.reshape(n,n))
print("Matrix A*B")
print(c.reshape(n, n))

