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


# Gateway


class PayGateway(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class Zarinpal(PayGateway):
    def pay(self, amount):
        print(f'paying {amount} via zarinpal...')


class Stripe(PayGateway):
    def pay(self, amount):
        print(f'paying {amount} vai stripe...')


def process_payment(gateway: PayGateway):
    gateway.pay(100)


# process_payment(Zarinpal())
# process_payment(Stripe())


# test abstract class session 10 training 6


class Employee(ABC):
    @abstractmethod
    def calculate_salary(self, hour):
        pass


class HourlyEmployee(Employee):
    def calculate_salary(self, hour):
        print(f'your salary this month: \n {hour} hour: {hour * 10}')


class SalariedEmployee(Employee):
    def calculate_salary(self, hour=160):
        print(f'your salary is for 160 hour in month: \n {hour} hour: {hour * 10}')


# he = HourlyEmployee()
# se = SalariedEmployee()
#
# he.calculate_salary(10)
# se.calculate_salary()


class Car2(ABC):
    def __init__(self, brand):
        self.brand = brand

    @abstractmethod
    def start(self):
        """this method muss be implemented...!"""

    @abstractmethod
    def stop(self):
        """this method muss be implemented...!"""


class SportCar2(Car2):
    def __init__(self, brand):
        super().__init__(brand)

    def start(self):
        print(f'{self.__class__.__name__} starting...!')

    def stop(self):
        print(f'{self.__class__.__name__} stopping...!')


class SedanCar2(Car2):
    def __init__(self, brand):
        super().__init__(brand)

    def start(self):
        print(f'{self.__class__.__name__} starting...!')

    def stop(self):
        print(f'{self.__class__.__name__} stopping...!')

# ---

class Person(ABC):
    def __init__(self, name, age, rol):
        self.name = name
        self._age = age
        self.rol = rol

    @abstractmethod
    def greet(self):
        """This method muss be implemented...!"""

    @abstractmethod
    def introduce(self):
        """This method muss be implemented...!"""


class Student(Person):
    def __init__(self, name, age, rol):
        super().__init__(name, age, rol)

    def greet(self):
        print(f'Hello class ...!')

    def introduce(self):
        print(f'my name is {self.name} and {self._age} years old, I am {self.rol} in '
              f'theses class ...!')


class Teacher(Person):
    def __init__(self, name, age, rol):
        super().__init__(name, age, rol)

    def greet(self):
        print(f'Hello my class ...!')

    def introduce(self):
        print(f'my name is {self.name} and {self._age} years old, I am your {self.rol} in'
              f'theses class ...!')
