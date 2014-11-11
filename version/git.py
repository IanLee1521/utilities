"""
Python functions for grabbing version strings and information out of GIT
"""

import datetime
import os
import subprocess


def sha1_hash(hash_format="H"):
    """
    Returns an alphanumeric identifier of the latest git hash.
    """
    repo_dir = os.path.dirname(os.path.abspath(__file__))
    git_log = subprocess.Popen(
        'git log --pretty=format:%{} --quiet -1 HEAD'.format(hash_format),
        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        shell=True, cwd=repo_dir, universal_newlines=True)
    git_hash = git_log.communicate()[0]

    if not git_hash:
        git_hash = 'unknown'

    return git_hash


def sha1_hash_short():
    """
    Returns an alphanumeric identifier of the latest git hash.
    """
    return sha1_hash("h")


def changeset():
    """
    Returns a numeric identifier of the latest git changeset.

    The result is the UTC timestamp of the changeset in YYYYMMDDHHMMSS format.
    This value isn't guaranteed to be unique, but collisions are very unlikely,
    so it's sufficient for generating the development version numbers.
    """
    repo_dir = os.path.dirname(os.path.abspath(__file__))
    git_log = subprocess.Popen(
        'git log --pretty=format:%ct --quiet -1 HEAD',
        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        shell=True, cwd=repo_dir, universal_newlines=True)
    timestamp = git_log.communicate()[0]
    try:
        timestamp = datetime.datetime.utcfromtimestamp(int(timestamp))
    except ValueError:
        return None
    return timestamp.strftime('%Y%m%d%H%M%S')
