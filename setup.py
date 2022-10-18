#!/usr/bin/env python
import ast
import os
import re
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open("requirements.txt") as fh:
    requirements = [r for r in fh.read().split("\n") if ";" not in r]

setup(
    name="code-combat-client",
    version="3",
    description="",
    author="@hexylena",
    author_email="hexylena@galaxians.org",
    packages=["combat"],
    install_requires=requirements,
    license="AGPL-3.0",
    zip_safe=True,
    keywords="code-combat-client",
)
