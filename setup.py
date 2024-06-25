#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

import os
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

requirement_path = os.path.dirname(os.path.realpath(__file__)) + '/requirements.txt'
install_requires = []
if os.path.isfile(requirement_path):
    with open(requirement_path) as f:
        install_requires = list(f.read().splitlines())

setup(
    name="doc_tester",
    version="0.1.0",
    author="Kurt Brendlinger",
    author_email="kurt.brendlinger@gmail.com",
    description="Package for testing documentation via Sphinx",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
            'Programming Language :: Python :: 3.10',
        ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    include_package_data=True,
    python_requires=">=3.10",
    install_requires=install_requires,
    )
