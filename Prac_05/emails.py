"""
CP1404 Practical
Email / Name Scanner.
"""

email_input = 0
email_matrix = {}

email_input = input("Enter your email: ")

while email_input != '':
    potential_name = email_input[0:email_input.index("@")].replace(".", " ")

    name_confirm = input("Is your name {}? [y|n]: ".format(potential_name))

    if name_confirm == "y" or name_confirm == "":
        email_matrix[email_input] = potential_name
    elif name_confirm == "n":
        email_matrix[email_input] = input("What is your name? ")

    email_input = input("Enter your email: ")

for email in email_matrix:
    print("{} ({})".format(email_matrix[email], email))

"""
    Email: lindsay.ward@jcu.edu.au
    Is your name Lindsay Ward? (Y/n)
    Email: abe@gmail.com
    Is your name Abe? (Y/n) y
    Email: jimbo546@hotmail.com
    Is your name Jim546? (Y/n) no
    Name: Jim Boh
    Email: 
    
    Lindsay Ward (lindsay.ward@jcu.edu.au)
    Abe (Abe@gmail.com)
    Jim Boh (jimbo546@hotmail.com)
"""
