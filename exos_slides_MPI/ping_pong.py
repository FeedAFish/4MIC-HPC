#!/usr/bin/env python3
from mpi4py import MPI
import numpy as np
import time

comm = MPI.COMM_WORLD
size = comm.size
rank = comm.rank

print( "I am rank %d in group of %d processes."%(rank,size) )

comm.Barrier(); time.sleep(1)

#------------------------------------------------------------------------------
#  Simple message exchange
#------------------------------------------------------------------------------

if rank == 0:
	comm.send(rank, dest=1, tag=11)
	msg = comm.recv(source=1, tag=12)
elif rank == 1:
	msg = comm.recv(source=0, tag=11)
	comm.send(rank, dest=0, tag=12)

if rank <= 1:
	print("Rank %d received a message from rank %d."%(rank, msg))

comm.Barrier(); time.sleep(1)

#------------------------------------------------------------------------------
#  Simple message exchange using dictionnary data
#------------------------------------------------------------------------------

meta = {'rank': rank}

if rank == 0:
	comm.send(meta, dest=1, tag=11)
	msg = comm.recv(source=1, tag=12)
elif rank == 1:
	msg = comm.recv(source=0, tag=11)
	comm.send(meta, dest=0, tag=12)

if rank <= 1:
	print("Rank %d received a message from rank %d." % (rank, msg['rank']))

comm.Barrier(); time.sleep(1)

#-------------------------------------------------------------------------------
#  Simple message exchange using numpy arrays
#-------------------------------------------------------------------------------

n = 100000
data = np.full (n, rank, dtype=np.int32)
buff = np.empty(n      , dtype=np.int32)

if rank == 0:
	comm.Send(data, dest  =1, tag=11)
	comm.Recv(buff, source=1, tag=12)
elif rank == 1:
	comm.Recv(buff, source=0, tag=11)
	comm.Send(data, dest  =0, tag=12)

if rank <= 1:
	print("Rank %d received an array filled with %d" % (rank, buff[0]))