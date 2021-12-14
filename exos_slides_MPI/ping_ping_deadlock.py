#!/usr/bin/env python3
from mpi4py import MPI
import numpy as np
import time

comm = MPI.COMM_WORLD
size = comm.size
rank = comm.rank

print( "I am rank %d in group of %d processes."%(rank,size) )

comm.Barrier(); time.sleep(1)

for n in [2**p for p in range(12)]:
	data = np.full (n, rank, dtype=np.float64)
	buff = np.empty(n,       dtype=np.float64)

	if rank == 0:
		comm.Send(data, dest  =1, tag=11)
		comm.Recv(buff, source=1, tag=12)
	elif rank == 1:
		comm.Send(data, dest  =0, tag=12)
		comm.Recv(buff, source=0, tag=11)

	print("Rank %d received vector of size %d" % (rank, n))
	comm.barrier()
