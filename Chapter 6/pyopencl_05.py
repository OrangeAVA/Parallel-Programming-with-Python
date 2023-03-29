import numpy as np
import pyopencl as cl
import pyopencl.array
from pyopencl.elementwise import ElementwiseKernel

import os
os.environ['PYOPENCL_CTX'] = '0'

a_host = np.array([0.1 , 1.4, 2.3, 1.7])
a_host = a_host.astype(np.float32)
b_host = np.array([0.2 , 0.3, 1.0, 0.5])
b_host = b_host.astype(np.float32)

ctx = cl.create_some_context()
queue = cl.CommandQueue(ctx)

a_dev = cl.array.to_device(queue, a_host)
b_dev = cl.array.to_device(queue, b_host)

sum = ElementwiseKernel(ctx,
    "float *a_dev, float *b_dev, float *res_dev",
    "res_dev[i] = a_dev[i] + b_dev[i]",
    "sum")

res_dev = cl.array.empty_like(a_dev)
sum(a_dev, b_dev, res_dev)

print("Vector A: %s" %a_host)
print("Vector B: %s" %b_host)
print("Vector Result: %s" %res_dev)

