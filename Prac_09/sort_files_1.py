"""
CP1404 Practical
File sorting program.
"""

import os
import shutil


def main():
    """Sort files into directories based on there file type, create directories where none exist."""
    os.chdir('FilesToSort')
    file_types = set([])
    directories = []

    filenames = os.listdir('.')

    for filename in filenames:
        if os.path.isdir(filename):
            continue
        file_type = filename.split(".")[1]
        try:
            shutil.move(filename, file_type + "/" + filename)
        except FileNotFoundError:
            os.mkdir(file_type)
            shutil.move(filename, file_type)


main()

