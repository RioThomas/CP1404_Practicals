
# Password Checker


def main():
    min_len = 5
    max_len = 20

    password = get_password(max_len, min_len)
    star_list = ""

    while min_len > len(password) or len(password) > max_len:
        password = get_password(max_len, min_len)

    star_print(password, star_list)


def star_print(password, star_list):
    for x in range(0, len(password)):
        star_list = star_list + "*"
    print(star_list)


def get_password(max_len, min_len):
    password = input("Enter a password between {} and {} characters long: ".format(max_len, min_len))
    return password


main()
