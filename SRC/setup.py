#!/usr/bin/env python
# Copyright (C) 2018 stryngs.

from setuptools import setup

setup(
    name = 'easy-thread',
    version = '0.8',
    author = 'stryngs',
    author_email = 'info@ethicalreporting.org',
    packages = ['easyThread'],
    include_package_data = True,
    url = 'https://github.com/stryngs/easy-thread',
    license ='GNU General Public License v2',
    keywords = 'python3 python2 python threading queue',
    description='An easy way to create a threaded queue for Python 2 or 3'
)
