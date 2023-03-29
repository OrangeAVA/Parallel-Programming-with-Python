import time
from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.rank
print("The process %d is started" %rank)
n = 0
for i in range(100000000):
   n += i
print("The process %d is ended" %rank)
