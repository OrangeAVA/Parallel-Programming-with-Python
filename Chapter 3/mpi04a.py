from mpi4py import MPI
import random
comm = MPI.COMM_WORLD
rank = comm.rank
if rank == 0:
   data=random.randint(1, 10)
else:
   data=None
data = comm.bcast(data, root=0)
if rank == 1:
   print("The square of %d is %d" %(data,data*data))
if rank == 2:
   print("Half of %d is %d" %(data,data/2))
if rank == 3:
   print("Double of %d is %d" %(data,data*2))
