
# Loops

for i in range(1, 21, 2):
    print(i, end=' ')

print()

for i in range(0, 101, 10):
    print(i, end=' ')

print()

for i in range(-20, 0):
    print(-i, end=' ')

print("\n")

star_num = int(input("Enter the number of Stars: "))
star_str = ""

for x in range(0, star_num):
    star_str = star_str + "*"
    print(star_str)
