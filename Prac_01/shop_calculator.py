
# SHOP CALCULATOR:
item_number = int(input("Enter the number of items: "))
while item_number <= 0:
    item_number = int(input("Please enter a valid value: "))

cost_array = []

for x in range(0 + 1, item_number + 1):
    cost_array.append(int(input("What is the price of item #{}? ".format(x))))

total_cost = sum(cost_array)

if total_cost > 100:
    total_cost = total_cost * 0.9

print("The total price for {} item/s is ${:.2f}".format(item_number, total_cost))
