#! /usr/bin/env python
# Copyright 2019 Spotify AB

import codecs
import os
import re

from setuptools import setup


HERE = os.path.abspath(os.path.dirname(__file__))


def get_package_meta(package_name, key):
    package = __import__(package_name)
    return getattr(package, "__{}__".format(key))


#####
# Project-specific constants
#####
NAME = "gcbd-sentinel"
PACKAGE_NAME = "gcbd_sentinel"
PACKAGES = [PACKAGE_NAME]


setup(
    name=NAME,
    version=get_package_meta(PACKAGE_NAME, "version"),
    description=get_package_meta(PACKAGE_NAME, "description"),
    url=get_package_meta(PACKAGE_NAME, "uri"),
    author=get_package_meta(PACKAGE_NAME, "author"),
    author_email=get_package_meta(PACKAGE_NAME, "email"),
    maintainer=get_package_meta(PACKAGE_NAME, "author"),
    maintainer_email=get_package_meta(PACKAGE_NAME, "email"),
    packages=PACKAGES,
    package_dir={"": "."},
    include_package_data=True,
    zip_safe=False,
    install_requires=read_requirements("requirements.txt"),
    test_suite="tests",
    tests_require=read_requirements("test-requirements.txt"),
)
