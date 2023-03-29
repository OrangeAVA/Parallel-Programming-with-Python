import time
from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.rank
print("The process %d is started" %rank)
time.sleep(10)
print("The process %d is ended" %rank)
