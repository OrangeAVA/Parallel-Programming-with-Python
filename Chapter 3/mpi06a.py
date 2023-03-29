from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.rank
if rank == 0: 
   data = 'AAA'
if rank == 1:
   data = 'BBB'
if rank == 2:
   data = 'CCC'
if rank == 3:
   data = 'DDD'
array = comm.gather(data, root=0)
if rank == 0:
   print("The new array is %s " %array)
