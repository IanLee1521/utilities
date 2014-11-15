#! /usr/bin/env python

import os


def get_files(path, ext=None):
    """
    Get all files in directory path, optionally with the specified extension
    """
    if ext is None:
        ext = ''

    return [
        os.path.abspath(fname)
        for fname in os.listdir(path)
        if os.path.isfile(fname)
        if fname.endswith(ext)
        ]
