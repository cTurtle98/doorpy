"""
doorpy - raspberry pi message board for your door
Copyright (C) 2020  Ciaran Farley (ciaran@cturtle98.com)

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

--------

setup.py - pypa setup file

"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
  long_description = f.read()

setup(
  name='doorpy',
  
  # VERSIONING SCHEMA
  # X.0.0 Major Release breaks compatability
  # 0.X.0 Minor release continues compatibility
  # 0.0.X Bug fix releases
  # 0.0.0.devX developement releases
  # 0.0.0.rcX release candidates
  version='1.0.0.dev1',
  
  # short description of project
  description='door mounted message board',
  
  # get long description from readme.md
  long_description=long_description,
  long_description_content_type='text/markdown',
  
  # url for the project source code
  url='https://github.com/cTurtle98/doorpy',
  
  # project author details
  author='Ciaran Farley'
  author_email='ciaran@cturtle98.com'
  
  classifiers=[
    
    # project maturity
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Developement Status :: 3 - Alpha',
    
    # project is made for use by
    'Intended Audience :: Other Audience',
    
    # project is written in english
    'Natural Language :: English',
    
    # this is the closest topic that makes sense
    'Topic :: Utilities',
    
    # gplv2 license
    'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
    
    # python 3.6 and up
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ].
  install_requires=['Flask'],
)

