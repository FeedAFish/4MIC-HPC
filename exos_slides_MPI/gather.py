#!/usr/bin/env python3
from mpi4py import MPI
import time

comm = MPI.COMM_WORLD
size = comm.size
rank = comm.rank

print( "I am rank %d in group of %d processes."%(rank,size) )

comm.Barrier(); time.sleep(1)

data = (rank+1)**rank

print( rank, data )

data = comm.gather(data, root=2)

print( rank, data )
