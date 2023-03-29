from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.rank
if rank==0:
   output = ['0A','0B','0C','0D']
if rank==1:
   output = ['1A','1B','1C','1D']
if rank==2:
   output = ['2A','2B','2C','2D']
if rank==3:
   output = ['3A','3B','3C','3D']

input = comm.alltoall(output)
print("Process %s received %s" %(rank,input))
