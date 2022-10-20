#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open("requirements.txt") as fh:
    requirements = [r for r in fh.read().split("\n") if ";" not in r]

setup(
    name="the-great-code-off",
    version="4",
    description="",
    author="@hexylena",
    author_email="hexylena@galaxians.org",
    packages=["tgco"],
    install_requires=requirements,
    license="AGPL-3.0",
    zip_safe=True,
)
