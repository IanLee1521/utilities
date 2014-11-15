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


def blob_text(filenames):
    """
    Create a blob of text by reading in all filenames into a string
    """
    return '\n'.join([open(fname).read() for fname in filenames])
