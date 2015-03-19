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
    """Create a blob of text by reading in all filenames into a string"""
    return '\n'.join([open(filename).read() for filename in filenames])


def get_definition(text, startswith):
    """Parse text to retrieve the definitions that start with keyword"""
    return [
        re.split('[ ()]', line.strip())[1]
        for line in [line.strip() for line in text.splitlines()]
        if line.startswith(startswith)
        ]


def get_functions(text, startswith='def '):
    """Parse text to retrive the functions and methods defined"""
    return get_definition(text, startswith)


def get_classes(text, startswith='class '):
    """Parse text to retrive the functions and methods defined"""
    return get_definition(text, startswith)


def find_options(filename):
    """
    Grab all of the ini style options in a specified file (ignoring sections)
    """
    with open(filename) as fp:
        text = [
            line for line in fp.readlines()
            if not line.startswith('#')
            if '=' in line
            ]
        return sorted(list(set(opt.split()[0] for opt in text)))


def find_functions(text):
    """Find all function names defined on all lines of the given text"""

    return list(set([
        re.split('[ (]*', line)[1]
        for line in [
            line.strip()
            for line in text.splitlines()
            if 'def ' in line
            ]
        if line.startswith('def ')
        ]))


def find_missing_keywords(keywords, text):
    """
    Return the subset of keywords which are missing from the given text
    """
    found = set()
    for key in keywords:
        if key in text:
            found.add(key)
    return list(set(keywords) - found)


def glob_filepath(path, ext=None):
    """
    Return all of the absolute filepaths in a given directory

    Optionally, return only those that end with ``ext``
    """

    if ext is None:
        ext = ''

    return [
        os.path.abspath(os.path.join(path, f))
        for f in os.listdir(path)
        if f.endswith(ext)
        ]


def find_missing_functions(keywords, text):
    """
    %timeit find_missing_funcs(funcs, text)
    1 loops, best of 3: 973 ms per loop
    """
    found = set()
    for line in text.splitlines():
        if not line.strip().startswith('def '):
            for f in keywords:
                if f in line:
                    found.add(f)
    return list(set(keywords) - found)


def find_used_modules(modules, text):
    """
    Given a list of modules, return the set of all those imported in text
    """
    used = set()
    for line in text.splitlines():
        for mod in modules:
            if 'import' in line and mod in line:
                used.add(mod)
    return used


def reverse_readline(filename, buf_size=8192):
    """a generator that returns the lines of a file in reverse order

    Taken from srohde on Stack Overflow:
    http://stackoverflow.com/a/23646049/450858
    """
    with open(filename) as fh:
        segment = None
        offset = 0
        fh.seek(0, os.SEEK_END)
        total_size = remaining_size = fh.tell()
        while remaining_size > 0:
            offset = min(total_size, offset + buf_size)
            fh.seek(-offset, os.SEEK_END)
            buffer = fh.read(min(remaining_size, buf_size))
            remaining_size -= buf_size
            lines = buffer.split('\n')
            # the first line of the buffer is probably not a complete line so
            # we'll save it and append it to the last line of the next buffer
            # we read
            if segment is not None:
                # if the previous chunk starts right from the beginning of line
                # do not concact the segment to the last line of new chunk
                # instead, yield the segment first
                if buffer[-1] is not '\n':
                    lines[-1] += segment
                else:
                    yield segment
            segment = lines[0]
            for index in range(len(lines) - 1, 0, -1):
                yield lines[index]
        yield segment


def grep(lines, pattern=None):
    if pattern is None:
        pattern = r''

    regex = re.compile(pattern)
    for line in lines:
        if regex.search(line):
            yield line
