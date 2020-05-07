
# Each time, until they quit:
#   The user should be presented with a list of available taxis and get to choose one,
#   Then they can choose how far they want to drive,
#   At the end of each trip, show them the trip cost and add it to their bill.

from Prac_08.silver_service_taxi import SilverServiceTaxi
from Prac_08.taxi import Taxi

taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
bill = 0.00

print("Let's drive!")
user_input = input("q)uit, c)hoose taxi: ")

while user_input != "q":
    if user_input == "c":
        for i, taxi in enumerate(taxis):
            # if taxi.fuel > 0:
            print("[{}] {}".format(i, taxi))
        taxi_choice = int(input("Choose a taxi: "))
        current_taxi = taxis[taxi_choice]
        print("{} Selected".format(current_taxi.name))
        print("Bill to date: ${:.2f}".format(bill))
    elif user_input == "d":
        distance = int(input("How far: "))
        current_taxi.drive(distance)
        print("Your {} trip cost ${}".format(current_taxi.name, current_taxi.get_fare()))
        bill += current_taxi.get_fare()
        print("Current Bill: ${:.2f}".format(bill))
    user_input = input("q)uit, c)hoose taxi, d)rive: ")

print("Total Trip Cost: ${:.2f}".format(bill))
print("Taxis are now:")
for taxi in taxis:
    print(taxi)
