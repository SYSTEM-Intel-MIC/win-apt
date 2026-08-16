#!/usr/bin/env python3
"""Setup script for WinApt"""
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="winapt",
    version="1.0.0",
    author="WinApt Team",
    description="apt-like package manager for Windows (via winget and Chocolatey)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/winapt/winapt",
    packages=find_packages(),
    py_modules=["apt", "apt_get", "utils", "easter_eggs"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: System :: Software Distribution",
        "Topic :: System :: Systems Administration",
        "Topic :: Utilities",
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "apt=apt:main",
            "apt-get=apt_get:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
