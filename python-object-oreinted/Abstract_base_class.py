from abc import ABC, abstractmethod


# Abstract Base Class
class Vehicle(ABC):
    @abstractmethod
    def move(self):
        """this method should be implemented!!!"""
        print('Default...')

    @abstractmethod
    def repair(self):
        """this method should be implemented!!!"""

    def class_name(self):
        print(self.__class__)


class LandVehicle(Vehicle):
    @abstractmethod
    def brake(self):
        """this method should be implemented!"""


class AirVehicle(Vehicle):
    @abstractmethod
    def eject(self):
        """this method should be implemented!"""


class Car(LandVehicle):
    def move(self):
        super().move()

    def repair(self):
        print('Under Repair...')

    def brake(self):
        print('Braking...')


class Airplane(AirVehicle):
    def move(self):
        print('flying...')

    def repair(self):
        print('Under Repair...')

    def eject(self):
        print('Ejecting...')
