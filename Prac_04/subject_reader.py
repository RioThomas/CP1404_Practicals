"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    subject_data = ""
    for line in input_file:
        line = line.strip()             # Remove the \n
        parts = line.split(',')         # Separate the data into its parts
        parts[2] = int(parts[2])        # Make the number an integer (ignore PyCharm's warning)
        subject_data = subject_data + "{} is taught by {:12} with {:3} students.\n".format(parts[0], parts[1], parts[2])
    input_file.close()
    return subject_data


main()
