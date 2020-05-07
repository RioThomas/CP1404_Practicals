
from Prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Premium Taxi."""
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverTaxi instance, based on parent class Taxi."""
        super().__init__(name, fuel)
        self.price_per_km *= fanciness
        self.current_fare_distance = 0

    def get_fare(self):
        """Return the price for the taxi trip."""
        return self.flagfall + super().get_fare()

    def __str__(self):
        """Return a string like a Taxi, but with the new fare."""
        return "{} plus flagfall of ${:.2f} ".format(super().__str__(), self.flagfall)
