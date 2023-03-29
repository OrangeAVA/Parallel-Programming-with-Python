from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.rank

comm_3D = comm.Create_cart(dims = [3,3,3],
                           periods=[False,False,False],
                           reorder=False)
xyz = comm_3D.Get_coords(rank)
print ("In this 3D topology, process %s has coordinates %s " %(rank,xyz))
