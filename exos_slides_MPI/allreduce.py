#!/usr/bin/env python3
from mpi4py import MPI
import time

comm = MPI.COMM_WORLD
size = comm.size
rank = comm.rank

print( "I am rank %d in group of %d processes."%(rank,size) )

comm.Barrier(); time.sleep(1)

if rank == 0:
	value = 10
else:
	value = rank

value = comm.allreduce( sendobj=value, op=MPI.PROD )

print( "for rank %d, value = "%rank, value )