# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='sample',
    version='0.0.1',
    description='Sample package for Python-Guide.org',
    long_description=readme,
    author='Phil Adams',
    author_email='phil@philadams.net',
    url='https://github.com/philadams/samplemod',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

