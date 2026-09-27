class Car:
    def start(self):
        print("Car is starting")


class Bike:
    def start(self):
        print("Bike is starting")


class Bus:
    def start(self):
        print("Bus is starting")


def start_vehicle(vehicle):
    vehicle.start()


c = Car()
b = Bike()
bus = Bus()

start_vehicle(c)
start_vehicle(b)
start_vehicle(bus)