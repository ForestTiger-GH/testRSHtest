# -*- coding: utf-8 -*-

from setuptools import setup

setup(
   name='testing1',
   version='1.0',
   description='A useful module',
   author='Author Name',
   author_email='merkulov.dmit@gmail.com',
   packages=['testing'],  #same as name
   install_requires=['numpy', 'pandas'], #external packages as dependencies
)
