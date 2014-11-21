#! /usr/bin/env python

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
