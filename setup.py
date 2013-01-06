from distutils.core import setup


with open('README.txt') as f:
    readme = f.read()

setup(
    name='sample',
    version='0.0.1',
    author='Phil Adams',
    author_email='phil@philadams.net',
    url='https://github.com/philadams/samplemod',
    license='LICENSE.txt',
    description='TODO some new package short info',
    long_description=readme,
    packages=['sample'],
    scripts=['bin/samplescript'],
)

