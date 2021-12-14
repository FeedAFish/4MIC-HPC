#!/usr/bin/env python3
from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.size #comm.Get_size()
rank = comm.rank #comm.Get_rank()

print( "I am rank %d in group of %d processes."%(rank,size) )