from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.rank

if rank == 0:
  output = np.array([0,0,0,0])
if rank == 1:
  output = np.array([1,1,1,1])
if rank == 2:
  output = np.array([2,2,2,2])
if rank == 3:
  output = np.array([3,3,3,3])

print("Process %d. Sending %s" %(rank,output))
input = comm.reduce(output, root=0, op=MPI.SUM)
if rank == 0:
  print("The result of the parallel computation is %s" %(input))
