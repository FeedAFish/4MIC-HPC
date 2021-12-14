#!/usr/bin/env python3
from mpi4py import MPI
import time

comm = MPI.COMM_WORLD
size = comm.size
rank = comm.rank

print( "I am rank %d in group of %d processes."%(rank,size) )

comm.Barrier(); time.sleep(1)

if rank == 0:
   data = [(x+1)**x for x in range(size)]
   print('data that will be scattered:', data)
else:
   data = None

data = comm.scatter(data, root=0)

print('rank =', rank,', data =', data)
