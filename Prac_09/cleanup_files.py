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
            if old_name != new_name:
                print("{:55} {:10} {:<55}".format(old_name, "->", new_name))
                os.rename(old_name, new_name)


def clean_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = ""
    for pos, char in enumerate(filename):
        prev_char = filename[pos-1]
        if pos == 0:
            new_name += filename[pos].upper()
        elif char.isupper() and prev_char.islower():
            new_name += " " + char
        else:
            new_name += char
    new_name = new_name.title().replace(" ", "_").replace("Txt", "txt")
    return new_name


main()

