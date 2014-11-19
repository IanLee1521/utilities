#! /usr/bin/env python

from subprocess import Popen, PIPE


def launch(cmd):
    """
    Fork the specified command, returning a tuple of (stdout, stderr)
    """
    return Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE).communicate()


def get_stdout(cmd):
    """
    Fork the specified command, returning stdout
    """
    return launch(cmd)[0]
