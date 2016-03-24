#! /usr/bin/env python

import errno
import os

from subprocess import Popen, PIPE


def popen(cmd):
    """
    Fork the specified command, returning a tuple of (stdout, stderr)
    """
    return Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE).communicate()


def get_stdout(cmd):
    """
    Fork the specified command, returning stdout
    """
    return popen(cmd)[0]


def get_stderr(cmd):
    """
    Fork the specified command, returning stderr
    """
    return popen(cmd)[1]


def mkdir_p(path):
    """
    Python version of shell `mkdir -p`

    Taken from http://stackoverflow.com/a/600612/450858
    """
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise
