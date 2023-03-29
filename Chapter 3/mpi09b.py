could add new lines to the code.
from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.rank

comm_3D = comm.Create_cart(dims = [3,3,3],
                       periods =[False,False,False],
                       reorder=False)
xyz = comm_3D.Get_coords(rank)

if rank==12:
  print ("In this 3D topology, process %s has coordinates %s " %(rank,xyz))
  right,left = comm_3D.Shift(0,1)
  up,down = comm_3D.Shift(1,1)
  forward,backward = comm_3D.Shift(2,1)
  print("Neighbors (left-right): %s %s" %(left,right))
  print("Neighbors (up-down): %s %s" %(up,down))
  print("Neighbors (forward-backward): %s %s" %(forward,backward))

