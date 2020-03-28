"""

webpy module setup.py
By Ciaran Farley

"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
  long_description = f.read()

setup(
  name='doorpy',
  version='1.0.0.dev1',
  description='door mounted message board',
  long_description=long_description,
  long_description_content_type='text/markdown',
  url='https://github.com/cTurtle98/doorpy',
  author='Ciaran Farley'
  author_email='ciaran@cturtle98.com'
  
  classifiers=[
    'Developement Status :: 3 - Alpha',
    'Intended Audience :: DIYers',
    'Topic :: DIY :: digital-signage',
    
    
