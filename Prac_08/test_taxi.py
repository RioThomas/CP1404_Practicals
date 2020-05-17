
from Prac_08.taxi import Taxi

# Create a new taxi with name "Prius 1", 100 units of fuel and price of $1.23/km
new_taxi = Taxi("Prius 1", 100)

# Drive the taxi 40km
new_taxi.drive(40)

# Print the taxi's details and the current fare
print(new_taxi)

# Restart the meter (start a new fare) and then drive the car 100km
new_taxi.start_fare()
new_taxi.drive(100)

# Print the details and the current fare
print(new_taxi)
