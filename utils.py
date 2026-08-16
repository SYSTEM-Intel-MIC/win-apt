"""Utility functions for WinApt"""
import sys
import os
import shutil

def is_admin():
    """Check if running as administrator"""
    try:
        import ctypes
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_as_admin(cmd):
    """Run command as administrator"""
    if sys.platform == "win32":
        import ctypes
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, cmd, None, 1)
    else:
        os.system(f"sudo {cmd}")

def ensure_admin():
    """Ensure running as admin, exit if not"""
    if not is_admin():
        print("This operation requires administrator privileges.")
        print("Please run as administrator.")
        sys.exit(1)

def get_terminal_width():
    """Get terminal width"""
    try:
        import shutil
        return shutil.get_terminal_size().columns
    except:
        return 80

def print_table(headers, rows):
    """Print a simple table"""
    if not rows:
        return

    col_widths = [len(h) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            col_widths[i] = max(col_widths[i], len(str(cell)))

    # Print header
    header_line = " | ".join(h.ljust(col_widths[i]) for i, h in enumerate(headers))
    print(header_line)
    print("-" * len(header_line))

    # Print rows
    for row in rows:
        print(" | ".join(str(cell).ljust(col_widths[i]) for i, cell in enumerate(row)))
