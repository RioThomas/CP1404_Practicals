
numbers = []

for i in range(1, 6):
    numbers.append(int(input("Enter Number {}: ".format(i))))

num_sum = sum(numbers)
num_avg = num_sum / 5
num_dif = max(numbers) - min(numbers)
num_end = numbers[4]

print("The sum is {}\nThe average is {}\nThe difference between the max and min is {}\nThe last number is {}".format(num_sum, num_avg, num_dif, num_end))

print("*******************************************")
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
user_input = input("Enter Username: ")

if user_input in usernames:
    print("ACCESS GRANTED")
else:
    print("ACCESS DENIED")



