"""
CP1404 Practical
File sorting program.
"""

import os
import shutil


def main():
    """Sort files into directories based on there file type, create directories where none exist."""
    os.chdir('FilesToSort')

    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            # Skip if it's a directory.
            continue
        file_type = filename.split(".")[1]
        try:
            # Try move file to file type directory.
            shutil.move(filename, file_type + "/" + filename)
        except FileNotFoundError:
            # If destination does not exist create it.
            os.mkdir(file_type)
            shutil.move(filename, file_type)


main()

