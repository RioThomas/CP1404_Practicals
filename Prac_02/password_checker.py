
# CP1404 - Practical 01
# PASSWORD CHECKER

MIN_LENGTH = 2
MAX_LENGTH = 10
SPECIAL_CHARS_REQUIRED = True
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print("Your password must be between {} and {} characters, and contain:".format(MIN_LENGTH, MAX_LENGTH))
    print("\t 1 or more uppercase characters")
    print("\t 1 or more lowercase characters")
    print("\t 1 or more numbers")

    if SPECIAL_CHARS_REQUIRED:
        print("\t and 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print("Your {}-character password is valid: {}".format(len(password), password))


def is_valid_password(password):
    """Determine if the provided password is valid."""
    # Check length against CONSTANTS:
    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        return False

    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0

    for char in password:
        # Count each kind of character:
        if char.isdigit():
            count_digit += 1
        elif char.isupper():
            count_upper += 1
        elif char.islower():
            count_lower += 1
        elif char in SPECIAL_CHARACTERS:
            count_special += 1

    # Check if any of the 'normal' counts are zero, if so return False:
    if count_upper == 0 or count_lower == 0 or count_digit == 0:
        return False

    # Check if special characters are required and if so if they;re present:
    if SPECIAL_CHARS_REQUIRED and count_special == 0:
        return False

    # If we get here (without returning False), then the password must be valid
    return True


main()
