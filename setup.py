#! /usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


setup(
    name='folklore_config',
    version='0.2.0',
    description='The Folklore service framework configuration module',
    long_description=open("README.rst").read(),
    author="maralla",
    author_email="maralla.ai@gmail.com",
    packages=find_packages(),
    package_data={'': ['LICENSE', 'README.rst']},
    url='https://github.com/maralla/folklore-config',
    install_requires=[
        'PyYAML'
    ]
)
