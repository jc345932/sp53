"""
CP1404/CP5632 Practical
Client code to use the Car class
Note that the import has a folder (module) in it.
"""
from workshopP7.car import Car


def main():
    bus = Car("Bus", 180)
    bus.drive(30)
    print("fuel =", bus.fuel, "odometer =", bus.odometer)
    print(bus)

    limo = Car("Limo", 100)
    limo.add_fuel(20)
    limo.drive(115)
    print("fuel =", limo.fuel, "odometer =", limo.odometer)
    print(limo)

main()