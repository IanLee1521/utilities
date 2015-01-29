#! /usr/bin/env python

import os


def all_subpaths(path):
    """Return a list of all subpaths of given path

    The returned list will be in the order of [os.curdir, ... , '/']
    """
    path = os.path.abspath(path)
    head, _ = os.path.split(path)
    paths = []
    while head != '/':
        paths.append(head)
        head, _ = os.path.split(head)
    return paths


def all_subpaths_iter(path):
    """Return an iterator of all subpaths of given path

    The returned list will be in the order of [os.curdir, ... , '/']
    """
    path = os.path.abspath(path)
    head, _ = os.path.split(path)
    while head != '/':
        yield head
        head, _ = os.path.split(head)
