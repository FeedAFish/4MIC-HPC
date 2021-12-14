#!/usr/bin/env python3

from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.size
rank = comm.rank

print("I am rank %d in group of %d processes, sending to %d 1000+rank"%( rank, size,(rank+1)%size ) )

comm.send( 1000+rank, dest = (rank+1)%size )
valeur = comm.recv( source = (rank-1)%size )

print( "I am rank %d in group of %d processes, receivng from %d, value = %d"%( rank, size,(rank-1)%size, valeur ) )