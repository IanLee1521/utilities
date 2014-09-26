#! /usr/bin/env python

from mpi4py import MPI


comm = MPI.COMM_WORLD


def get_host():
    return MPI.Get_processor_name()


def get_rank():
    return comm.Get_rank()


def finalize():
    return MPI.Finalize()
