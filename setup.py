#!/usr/bin/env python

from setuptools import setup
setup(
    name='BayesCNN',
    version='0.1dev',
    author='Mohamed Abdel Aziz, Mehmood Alam Khan',
    author_email='mohamed.abdelaziz@ericsson.com, malagori@kth.se',
    url='https://github.com/malagori/BayesCNN',
    packages=['bayesCNN',],
    scripts = ['runBayesCNN.py',],
    license='GPLv3',
    long_description=open('README.md').read(),
    install_requires= ['numpy>=1.11.1'],
)