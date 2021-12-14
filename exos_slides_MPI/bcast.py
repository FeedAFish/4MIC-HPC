#!/usr/bin/env python3s
from mpi4py import MPI
import time

comm = MPI.COMM_WORLD
size = comm.size
rank = comm.rank

print( "I am rank %d in group of %d processes."%(rank,size) )

comm.Barrier(); time.sleep(1)

#------------------------------------------------------------------------------
# Perform Bcast / first version
#------------------------------------------------------------------------------

if rank == 0:
	data = {'a':1,'b':2,'c':3}
else:
	data = None

print( 'rank =', rank, ', data =', data )
comm.Barrier(); time.sleep(1)

data = comm.bcast(data, root=0)

print( 'rank =', rank, ', data =', data )
comm.Barrier(); time.sleep(1)

#------------------------------------------------------------------------------
# Perform Bcast / second version
#------------------------------------------------------------------------------

if rank == 0:
	data = {'a':1,'b':2,'c':3}
	print( 'rank =', rank, ', data =', data )
	comm.bcast(data, root=0)
else:
	print( 'rank =', rank, ', data =', data )
	data = comm.bcast(None, root=0)

print( 'rank =', rank, ', data =', data )
