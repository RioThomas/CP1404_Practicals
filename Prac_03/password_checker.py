
# Password Checker

MIN_LEN = 5
MAX_LEN = 20


def main():
    password = get_password(MAX_LEN, MIN_LEN)
    star_print(password)


def star_print(text_to_replace):
    print('*' * len(text_to_replace))


def get_password(max_len, min_len):
    password = ''
    while min_len > len(password) or len(password) > max_len:
        password = input("Enter a password between {} and {} characters long: ".format(max_len, min_len))
    return password


main()
