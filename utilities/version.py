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


def pep386(version):
    """
    Returns a PEP 386-compliant version number from VERSION

    Given a 5 tuple of (X, Y, Z, rel, N) return a PEP-386 compliant version
    string. rel should be one of ('alpha', 'beta', 'rc', 'final')
    """
    assert len(version) == 5
    assert version[3] in ('alpha', 'beta', 'rc', 'final')

    # Now build the two parts of the version number:
    # main = X.Y[.Z]
    # sub = .devN - for pre-alpha releases
    #     | {a|b|c}N - for alpha, beta and rc releases

    parts = 2 if version[2] == 0 else 3
    main = '.'.join(str(x) for x in version[:parts])

    sub = ''
    if version[3] == 'alpha' and version[4] == 0:
        git_changeset = changeset()
        if git_changeset:
            sub = '.dev%s' % git_changeset

    elif version[3] != 'final':
        mapping = {'alpha': 'a', 'beta': 'b', 'rc': 'c'}
        sub = mapping[version[3]] + str(version[4])

    return str(main + sub)
