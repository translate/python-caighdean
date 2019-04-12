#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Python caighdean
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages


install_requires = ["requests", "sacremoses"]
extras_require = {}
extras_require['test'] = [
    "pytest",
    "pytest-mock",
    "requests_mock",
    "coverage",
    "pytest-cov<2.6",
    "codecov",
    "flake8"],

setup(
    name='caighdean',
    version='0.0.4',
    description='Python Caighdean',
    long_description="Python caighdean",
    url='https://github.com/translate/python-caighdean',
    author='Ryan Northey',
    author_email='ryan@synca.io',
    license='GPL3',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        ('License :: OSI Approved :: '
         'GNU General Public License v3 or later (GPLv3+)'),
        'Programming Language :: Python :: 2.7',
    ],
    keywords='python caighdean',
    install_requires=install_requires,
    extras_require=extras_require,
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    include_package_data=True)
