"""
CP1404 Practical
File name cleaning program.
"""

import os


def main():
    """Clean file names to ensure correct naming conventions."""
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        for filename in filenames:
            new_name = os.path.join(directory_name, clean_filename(filename))
            old_name = os.path.join(directory_name, filename)
            print("{:50} {:<50}".format(old_name, new_name))
            os.rename(old_name, new_name)


def clean_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = ""
    for pos, char in enumerate(filename):
        if filename[pos].isupper() and filename[pos-1].islower():
            new_name += " " + filename[pos]
        else:
            new_name += filename[pos]
    new_name = new_name.title().replace(" ", "_").replace("Txt", "txt")[1:]
    return new_name


main()

