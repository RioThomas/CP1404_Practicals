
from Prac_08.unreliable_car import UnreliableCar

old_car = UnreliableCar("DeLorean", 500, 70)
bad_car = UnreliableCar("Go-Cart", 20, 30)

print("Make 10 x 50km trips with old car:")
for x in range(10):
    old_car.drive(50)
    print(old_car)

print("\nMake 10 x 50km trips with bad car:")
for x in range(10):
    bad_car.drive(1)
    print(bad_car)
