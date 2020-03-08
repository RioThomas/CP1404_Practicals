
# CP1404 - Practical
# Answer the following questions:
# 1. When will a ValueError occur?
# 2. When will a ZeroDivisionError occur?
# 3. Could you change the code to avoid the possibility of a ZeroDivisionError?

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    while denominator == 0:
        denominator = int(input("The denominator can't be 0, choose a new number: "))

    fraction = numerator / denominator
    print(fraction)

except ValueError:
    print("Numerator and denominator must be valid numbers!")

except ZeroDivisionError:
    print("Cannot divide by zero!")

print("Finished.")


# ANSWERS:
# 1 : ValueError occurs when a non-int input is given to the program.
# 2 : ZeroDivisionError is when the denominator is set to be 0.
# 3 : Added while loop to handle a 0 divisor.
