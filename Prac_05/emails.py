"""
CP1404 Practical
Email / Name Scanner.
"""


def main():
    email_matrix = {}
    email_input = input("Enter your email: ")

    while email_input != '':
        potential_name = extract_name_from_email(email_input)

        user_confirmation = input("Is your name {}? [y|n]: ".format(potential_name)).lower()
        if user_confirmation == "y" or user_confirmation == "":
            # Potential name was correct, assign to email.
            email_matrix[email_input] = potential_name
        elif user_confirmation == "n":
            # Potential name was incorrect, ask user for name.
            email_matrix[email_input] = input("Name: ")
        else:
            print("Invalid Input.")

        email_input = input("Enter your email: ")

    print("")
    for email_entry in email_matrix:
        # Print the name & email. Format: John Wick (john.wick@hitmail.com)
        print("{} ({})".format(email_matrix[email_entry], email_entry))


def extract_name_from_email(email):
    # 1. Slice it from the start to the @
    # 2. Then replace any dots with spaces
    # 3. Then capitalise the start of each word.
    name = email[0:email.index("@")]\
        .replace(".", " ")\
        .title()
    return name


main()

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
