#!/usr/bin/env python3
"""WinApt - apt for Windows

This is the main entry point for the 'apt' command.
It provides an apt-like interface to Windows package managers (winget, Chocolatey).
"""
import sys
import os

# Add the script directory to path for imports
script_dir = os.path.dirname(os.path.abspath(__file__))
if script_dir not in sys.path:
    sys.path.insert(0, script_dir)

from core.parser import AptParser
from core.executor import AptExecutor

def main():
    parser = AptParser(prog_name="apt")
    args = parser.parse()

    executor = AptExecutor(prog_name="apt")
    return executor.execute(args)

if __name__ == "__main__":
    sys.exit(main())
