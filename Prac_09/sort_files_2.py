"""
CP1404 Practical
File sorting program.
"""

import os
import shutil


def main():
    """Sort files into user customised categories based on there file type, create directories where none exist."""
    os.chdir('FilesToSort')
    file_types = set([])
    file_type_dict = {}

    file_names = os.listdir('.')

    for file_name in file_names:
        # Create a set of all the file types:
        if os.path.isdir(file_name):
            continue
        file_type = file_name.split(".")[1]
        file_types.add(file_type)

        if file_type not in file_type_dict:
            # Ask the user what category they would like to sort the file type into:
            super_type = input("Where would you like {} to go? ".format(file_type))
            file_type_dict[file_type] = super_type

        file_category = file_type_dict[file_type]
        try:
            # Try move file to category directory:
            shutil.move(file_name, file_category + "/" + file_name)
        except FileNotFoundError:
            # Create directory then move if it doesn't exist:
            os.mkdir(file_category)
            shutil.move(file_name, file_category)

    # Data to test with:
    # file_type_dict = {'jpg': 'images', 'gif': 'images', 'xls': 'data', 'xlsx': 'data', 'doc': 'text', 'docx': 'text',
    #                   'txt': 'text', 'png': 'images'}


main()

