
from Prac_08.silver_service_taxi import SilverServiceTaxi

# For an 18km trip in a SilverServiceTaxi with fanciness of 2, the fare should be $48.78 (yikes!)

premium_taxi = SilverServiceTaxi("Premium Taxi", 200, 2)
print(premium_taxi)
premium_taxi.drive(18)
print(premium_taxi.get_fare())
print(premium_taxi)
