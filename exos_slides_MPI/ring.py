#!/usr/bin/env python
from mpi4py import MPI
import time

comm = MPI.COMM_WORLD
size = comm.size
rank = comm.rank

print( "I am rank %d in group of %d processes."%(rank,size) )

comm.Barrier(); time.sleep(1)

#------------------------------------------------------------------------------
# Perform Ring
#------------------------------------------------------------------------------

if rank == 0:
	token = 0
	comm.send(token, dest=1, tag=11)
	token = comm.recv(source=size-1, tag=11)
	print("Rank %d received token from rank %d with value %d" % (rank, size-1, token))
else:
	token = comm.recv(source=rank-1, tag=11)
	print("Rank %d received token from rank %d and send to %d" % (rank, rank-1, (rank+1)%size))
	time.sleep(1)
	token = token + rank
	comm.send(token, dest=(rank+1)%size, tag=11)

#------------------------------------------------------------------------------
# Verification of final token value
#------------------------------------------------------------------------------

token = comm.allreduce(rank,op=MPI.SUM)

if rank == size-1:
	print("Theorical token Value %d"%(token))

comm.Barrier()