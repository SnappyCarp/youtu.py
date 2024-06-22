#!/usr/bin/env python
import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
descriptions = "rip off pytube and add my own features"

setup(
    name="youtu.py",
    version="1.0.0",
    author="SnappyCarp",
    author_email="nah@funny.fake",
    packages=find_packages(),
    url="https://github.com/SnappyCarp/youtu.py",
    license="The Unlicense (Unlicense)",
    description=(descriptions),
    long_description_content_type="text/markdown",
    long_description=descriptions,
    zip_safe=True,
    python_requires=">=3.7",
)
