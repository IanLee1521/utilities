#! /usr/bin/env python

import os
import re


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


def get_definition(text, startswith):
    """
    Parse text to retrieve the definitions that start with keyword
    """
    return [
        re.split('[ ()]', line.strip())[1]
        for line in [line.strip() for line in text.splitlines()]
        if line.startswith(startswith)
        ]


def get_functions(text, startswith='def '):
    """
    Parse text to retrive the functions and methods defined
    """
    return get_definition(text, startswith)


def get_classes(text, startswith='class '):
    """
    Parse text to retrive the functions and methods defined
    """
    return get_definition(text, startswith)
