#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) Pootle contributors.
#
# This file is a part of the Pootle project. It is distributed under the GPL3
# or later license. See the LICENSE file for a copy of the license and the
# AUTHORS file for copyright and authorship information.

"""Python caighdean
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages

setup(
    name='caighdean',
    version='0.0.1',
    description='Python Caighdean',
    long_description="Python caighdean",
    url='https://github.com/phlax/caighdean',
    author='Ryan Northey',
    author_email='ryan@synca.io',
    license='GPL3',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: GPL3',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='python caighdean',
    install_requires=[
        "nltk",
        "pytest",
        "pytest-mock",
        "requests_mock",
        "coverage",
        "pytest-coverage",
        "codecov",
        "flake8"],
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    include_package_data=True)
