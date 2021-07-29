#! /usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup


setup(
    name='utilities',
    version='0.1',
    description='Utilities for common development tasks',
    author='Ian Lee',
    author_email='IanLee1521@gmail.com',
    license='MIT License',
    packages=['utilities'],
    entry_points={
        'console_scripts': [
            'find_duplicates = utilities.find_duplicates:main',
            'fix_numbering = utilities.fix_numbering:main',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
