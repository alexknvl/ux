#!/usr/bin/env python

from distutils.core import setup

setup(name='osunlp-ux',
      version='0.2',
      description='extra tools',
      author='Alexander Konovalov',
      author_email='alex.knvl@gmail.com',
      packages=['ux'],
      install_requires=[
          'namedlist',
          'osunlp-easytime'
      ])
