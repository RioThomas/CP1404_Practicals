
from Prac_08.car import Car
from random import randint


class UnreliableCar(Car):
    """Create an unreliable car that has a chance to fail every time it is driven.
    The chance to fail is based on the reliability which is assigned to the object on creation."""

    def __init__(self, name, fuel, reliability):
        """Initialise a unreliable car instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability
        self.failed = False

    def drive(self, distance):
        """Generate a random int between 0 and 100 and if it is less than
        the reliability factor the car will run, if not it will not drive."""
        if randint(0, 100) < self.reliability:
            self.failed = False
        else:
            self.failed = True
            distance = 0
            return 0
        super().drive(distance)

    def __str__(self):
        """ Print output in the form: Car, fuel = 42, odometer = 277"""
        fail_text = "(Failed)" if self.failed else ""
        return "{} {}".format(super().__str__(), fail_text)


