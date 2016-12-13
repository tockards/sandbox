#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 tockards <tockards@tockards-ska>
#
# Distributed under terms of the MIT license.

"""

"""
import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "daemonized",
    version = "0.0.1",
    author = "Toufeeq",
    author_email = "toufeeq.ockards@gmail.com",
    description = ("An demonstration of how to daemonize celery."
                                   "Why not."),
    license = "BSD",
    keywords = "example documentation tutorial",
    url = "tockards.github.io",
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
