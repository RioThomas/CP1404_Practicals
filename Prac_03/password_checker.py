
# Password Checker

MIN_LEN = 5
MAX_LEN = 20

password = input("Enter a password between {} and {} characters long: ".format(MIN_LEN, MAX_LEN))
star_list = ""

while MIN_LEN > len(password) or len(password) > MAX_LEN:
    password = input("Enter a valid password between {} and {} characters long:".format(MIN_LEN, MAX_LEN))

for x in range(0, len(password)):
    star_list = star_list + "*"

print(star_list)
