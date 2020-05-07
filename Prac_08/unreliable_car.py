
from Prac_08.car import Car
from random import randint


class UnreliableCar(Car):
    failed = False

    def __init__(self, name, fuel, reliability):
        """Initialise a unreliable car instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        if randint(0, 100) < self.reliability:
            self.failed = False
            if distance > self.fuel:
                distance = self.fuel
                self.fuel = 0
            else:
                self.fuel -= distance
            self.odometer += distance
            return distance
        else:
            self.failed = True
            return 0

    def __str__(self):
        """ Print output in the form: Car, fuel = 42, odometer = 277"""
        fail_text = "(Failed)" if self.failed else ""
        return "{}, fuel = {}, odometer = {} {}".format(self.name, self.fuel, self.odometer, fail_text)


