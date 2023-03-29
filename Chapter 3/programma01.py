from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.rank
print("Process %s started" %rank)
if rank==0:
   msg ="This is my message"
   receiver = 1
   comm.send(msg,dest=receiver)
   print("Process 0 sent: %s " %msg + "to %d" %receiver)    
if rank==1:
   source=0
   msg=comm.recv(source)
   print("Process 1 received is: %s" %msg + "from %d" %source)
