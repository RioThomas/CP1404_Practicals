# Fill in the TODOs to complete the task
# CP1404/CP5632 - Practical

finished = False
result = 0

while not finished:
    try:
        result = int(input("Input a integer: "))
        finished = True

    except ValueError:
        print("Please enter a valid integer.")

print("Valid result is:", result)
