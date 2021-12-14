#!/usr/bin/env python

from mpi4py import MPI

comm = MPI.COMM_WORLD

size = comm.size
rank = comm.rank

print("Rank %d/%d is sending to rank %d"%(rank, size, (rank+1)%size) )

valeur = comm.sendrecv(rank+1000,dest=(rank+1)%size)

print("Rank %d received valeur = %d"%(rank,valeur))