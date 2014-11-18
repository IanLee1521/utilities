#! /usr/bin/env python

from subprocess import Popen, PIPE


def _popen(cmd):
    """
    Fork the specified command, returning a tuple of (stdout, stderr)
    """
    return Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE).communicate()
