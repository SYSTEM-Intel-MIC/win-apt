#!/usr/bin/env python3
"""WinApt - apt-get for Windows

This is the entry point for the 'apt-get' command.
It provides an apt-get-like interface to Windows package managers.
"""
import sys
import os

# Add the script directory to path for imports
script_dir = os.path.dirname(os.path.abspath(__file__))
if script_dir not in sys.path:
    sys.path.insert(0, script_dir)

from core.parser import AptGetParser
from core.executor import AptExecutor

def main():
    parser = AptGetParser()
    args = parser.parse()

    executor = AptExecutor(prog_name="apt-get")
    return executor.execute(args)

if __name__ == "__main__":
    sys.exit(main())
