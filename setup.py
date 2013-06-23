#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
"""

    myip

    by hgschmidt

    Copyright (c) 2012 apitrary

"""
try:
    from setuptools import setup
    from setuptools import find_packages
except ImportError:
    import ez_setup

    ez_setup.use_setuptools()
    from setuptools import setup
    from setuptools import find_packages


def read_requirements():
    """
        Read the requirements.txt file
    """
    with open('requirements.txt') as f:
        requirements = f.readlines()
    return [element.strip() for element in requirements]


setup(
    name='myip',
    version='0.1.1',
    description='Python myip service by apitrary',
    long_description='myip is a simple web service presenting you your external IP address',
    author='Hans-Gunther Schmidt',
    author_email='hgs@apitrary.com',
    maintainer='apitrary',
    maintainer_email='official@apitrary.com',
    url='https://github.com/apitrary/myip',
    packages=find_packages('myip'),
    package_dir={'': 'myip'},
    scripts=[
        'myip/myip_runner.py'
    ],
    data_files=[
        ('/usr/local/share/myip/templates', ['myip/templates/base.html']),
        ('/usr/local/share/myip/templates', ['myip/templates/external.html']),
        ('/usr/local/share/myip/templates', ['myip/templates/local.html'])
    ],
    license='copyright by apitrary',
    install_requires=read_requirements()
)
