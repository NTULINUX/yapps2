#!/usr/bin/env python

from setuptools import setup
import os
from yapps import __version__ as version

pkg_root = os.path.dirname(__file__)

# Error-handling here is to allow package to be built w/o README included
try: readme = open(os.path.join(pkg_root, 'README.md')).read()
except IOError: readme = ''

setup(
    name = 'Yapps2',
    version = version,
    author = 'Amit J. Patel, Matthias Urlichs',
    author_email = 'amitp@cs.stanford.edu, smurf@debian.org',
    maintainer = 'Matthias Urlichs',
    maintainer_email = 'smurf@debian.org',
    license = 'MIT',
    url = 'https://github.com/smurfix/yapps',

    description = 'Yet Another Python Parser System',
    long_description = readme,

    packages = ['yapps'],
    include_package_data = True,
    package_data = {'': ['README.txt']},
    exclude_package_data = {'': ['README.*']},

    entry_points = dict(console_scripts=[
        'yapps2 = yapps.cli_tool:main' ]) )
