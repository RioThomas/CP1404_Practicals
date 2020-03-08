
# Files Practical Task:

# ### PART 1 ### #
name = str(input("What is your name? "))
f = open("data.txt", "w")
f.write(name)
f.close()

# ### PART 2 ### #
f = open("data.txt", "r")
print("your name is " + str(f.read()))
f.close()

# ### PART 3 ### #
f = open("numbers.txt", "w")
f.write("17\n42\n400")
f.close()

f = open("numbers.txt", "r")
num_1, num_2 = int(f.readline()), int(f.readline())
total = num_1 + num_2
print(total)
f.close()

# ### PART 4 ### #
f = open("numbers.txt", "r")
number_array = []

for x in f:
    number_array.append(int(x))

total = sum(number_array)
print(total)
f.close()