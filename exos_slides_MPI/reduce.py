#!/usr/bin/env python3

from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.rank

if rank == 0:
	value = 1000
else:
	value = rank

value = comm.reduce( sendobj=value, op=MPI.SUM, root=0 )

print( "for rank %d, value = "%rank, value )