#! /usr/bin/env python

from mpi4py import MPI


comm = MPI.COMM_WORLD


def get_host():
    """Get the hostname that this task is running on"""
    return MPI.Get_processor_name()


def get_rank():
    """Get the rank within all tasks mpi is running"""
    return comm.Get_rank()


def host_rank_mapping():
    """Get host to rank mapping

    Return dictionary mapping ranks to host
    """
    d = {}
    for (host, rank) in comm.allgather((get_host(), get_rank())):
        if host not in d:
            d[host] = []
        d[host].append(rank)
    return d


def finalize():
    return MPI.Finalize()
