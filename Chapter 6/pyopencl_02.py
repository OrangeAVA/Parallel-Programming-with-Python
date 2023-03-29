import numpy as np
import pyopencl as cl

a_host = np.array([0.1 , 1.4, 2.3, 1.7])
a_host = a_host.astype(np.float32)
res_host = np.zeros((4), dtype=np.float32)

ctx = cl.create_some_context()
queue = cl.CommandQueue(ctx)

mf = cl.mem_flags
a_dev = cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=a_host)
res_dev = cl.Buffer(ctx, mf.WRITE_ONLY, a_host.nbytes)

prg = cl.Program(ctx, """
__kernel void doubled(
    __global const float *a_dev, __global float *res_dev)
{
  int gid = get_global_id(0);
  res_dev[gid] = a_dev[gid]*2;
}
""").build()


knl = prg.doubled
knl(queue, a_host.shape, None, a_dev, res_dev)
cl.enqueue_copy(queue, res_host, res_dev)

print("Vector a: %s" %a_host)
print("Result: %s" %res_host)

