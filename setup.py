#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os

version = '0.1.1'
long_description = '\n'.join([
    open('README.rst').read(),
    ])

classifiers = [
    'Development Status :: 4 - Beta',
    'Environment :: Plugins',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Topic :: Software Development :: Libraries :: Python Modules',
]

setup(
    name='pygments-style-idleclassic',
    version=version,
    description='Pygments version of the Idle Classic theme.',
    long_description=long_description,
    classifiers=classifiers,
    keywords=['pygments', 'style', 'idle classic', 'syntax highlighting'],
    author='Matt Stark',
    author_email='mattstark75@gmail.com',
    url='https://github.com/matts1/pygments-style-idleclassic',
    license='MIT',
    packages=find_packages(),
    install_requires=['pygments >= 1.5'],
    entry_points="""
        [pygments.styles]
        idleclassic=pygments_style_idleclassic.idleclassic:IdleClassicStyle
    """,
    zip_safe=False,
)
