#!/usr/bin/env python3

""" This is the setup.py script for setting up the package and fulfilling any
necessary requirements.
"""

from setuptools import setup, find_packages
from codecs import open  # To use a consistent encoding
from os import path

# Set the home path of the setup script/package
home = path.abspath(path.dirname(__file__))
name = 'myrandomutils'


def readme():
    """Get the long description from the README file."""
    with open(path.join(home, 'README.md'), encoding='utf-8') as f:
        return f.read()


setup(
    name=name,
    author='Shaurita Hutchins',
    description="A package of my favorite python utility classes or functions.",
    version='0.3',
    long_description=readme(),
    url='https://github.com/sdhutchins/myrandomutils',
    license='MIT',
    keywords='science lab filemanagement',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Unix',
        'Natural Language :: English',
        'Programming Language :: Python :: 3 :: Only'
        ],
    # Packages will be automatically found if not in this list.
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
                'myrandomutils=myrandomutils.cli:myrandomutils'
                ]
    },
    install_requires=[
            'click>=7.0'
            ],
    zip_safe=False,
    test_suite='nose.collector',
    tests_require=['nose']
)
