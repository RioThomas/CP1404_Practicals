"""
CP1404 Practical
Email / Name Scanner.
"""

email_matrix = {}
email_input = input("Enter your email: ")

while email_input != '':
    # Slice the email from the start to the @, then remove any dots, and then capitalise each word.
    potential_name = email_input[0:email_input.index("@")].replace(".", " ").title()

    user_confirmation = input("Is your name {}? [y|n]: ".format(potential_name)).lower()

    if user_confirmation == "y" or user_confirmation == "":
        email_matrix[email_input] = potential_name
    elif user_confirmation == "n":
        email_matrix[email_input] = input("Name: ")

    email_input = input("Enter your email: ")

print("")

for email_entry in email_matrix:
    # Print the name & email. Format: John Wick (john.wick@hitmail.com)
    print("{} ({})".format(email_matrix[email_entry], email_entry))

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
