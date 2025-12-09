class Vehicle:
    def __init__(self, name: str, year: str, passenger: int, typ: str, color: str, weight: int, **kwargs) -> None:
        self.name = name
        self.year = year
        self.passenger = passenger
        self.typ = typ
        self.color = color
        self.weight = weight

    def __str__(self) -> str:
        return f'created: {self.year}, number of passenger: {self.passenger}, type: {self.typ}'

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.year}, {self.passenger}, {self.typ})'

    def move(self):
        pass

    def stop(self):
        pass

    def get_info(self):
        pass

class Car(Vehicle):
    def __init__(self, fuel_type: str, number_doors: int, engine_power: str, **kwargs):
        super().__init__(**kwargs)
        self.fuel_type = fuel_type
        self.number_doors = number_doors
        self.engine_power = engine_power

    def __str__(self):
        return f'{self.name}, created: {self.year}, fuel: {self.fuel_type}, engine: {self.engine_power}'

    def __repr__(self):
        return (f'{self.__class__.__name__}(name={self.name!r}, year={self.year!r}, passenger={self.passenger}, '
                f'typ={self.typ!r}, color={self.color!r}, weight={self.weight}, fuel_type={self.fuel_type!r}, '
                f'number_doors={self.number_doors}, engine_power={self.engine_power!r})')

    def move(self):
        print('moving car')

    def stop(self):
        print('stop car')

    def get_info(self):
        print(f'name={self.name}, year={self.year}, passenger={self.passenger}, typ={self.typ}, '
              f'color={self.color!r}, weight={self.weight}, fuel_type={self.fuel_type!r}, '
              f'number_doors={self.number_doors}, engine_power={self.engine_power}')

    def honk(self):
        print('boooooogh')


class Bicycle(Vehicle):
    def __init__(self, number_gears: int, has_basket: bool, bicycle_type: str, **kwargs):
        super().__init__(**kwargs)
        self.number_gears = number_gears
        self.has_basket = has_basket
        self.bicycle_type = bicycle_type

    def __str__(self):
        return f'{self.name}, created: {self.year}, color: {self.color}, type: {self.bicycle_type}'

    def __repr__(self):
        return (f'{self.__class__.__name__}(name={self.name!r}, year={self.year!r}, passenger={self.passenger}, '
                f'typ={self.typ!r}, color={self.color!r}, weight={self.weight}, number_gears={self.number_gears}, '
                f'has_basket={self.has_basket}, bicycle_type={self.bicycle_type!r})')

    def move(self):
        print('bicycle moving')

    def stop(self):
        print('bicycle stop')

    def get_info(self):
        print(f'name={self.name}, year={self.year}, passenger={self.passenger}, typ={self.typ}, color={self.color}, '
              f'weight={self.weight}, number_gears={self.number_gears}, has_basket={self.has_basket}, '
              f'bicycle_type={self.bicycle_type}')

    def ring_bell(self):
        print('riiiiiiing')

    def pedal(self):
        print('pedaling')
        self.move()


class Airplane(Vehicle):
    def __init__(self, wingspan: str, airline: str, **kwargs):
        super().__init__(**kwargs)
        self.wingspan = wingspan
        self.airline = airline

    def __str__(self):
        return f'{self.name}, created: {self.year}, airline: {self.airline}, wingspan: {self.wingspan}'

    def __repr__(self):
        return (f'{self.__class__.__name__}(name={self.name!r}, year={self.year!r}, passenger={self.passenger}, '
                f'typ={self.typ!r}, color={self.color!r}, weight={self.weight}, wingspan={self.wingspan}, '
                f'airline={self.airline}')

    def take_off(self):
        print(f'airplane take off')

    def land(self):
        print(f'airplane land')

    def move(self):
        self.take_off()

    def stop(self):
        self.land()


class Lamborghini(Car):
    def __init__(self, scissor_doors: bool, zero_to_hundred_time: int, **kwargs):
        super().__init__(**kwargs)
        self.scissor_doors = scissor_doors
        self.zero_to_hundred_time = zero_to_hundred_time

    def activate_sport_mode(self):
        print('activate_sport_mode')

    def deactivate_sport_mode(self):
        print('activate_sport_mode')

    def activate_sport_mode(self):
        print('activate_sport_mode')


class Benz(Car):
    def __init__(self, luxury_level: int, has_massage_seat: bool, brand_sign: str, **kwargs):
        super().__init__(**kwargs)
        self.luxury_level = luxury_level
        self.has_massage_seat = has_massage_seat
        self.brand_sign = brand_sign

    def turn_on_massage_seat(self):
        print('turn_on_massage_seat')

    def turn_off_massage_seat(self):
        print('turn_off_massage_seat')

    def honk(self):
        print('benz booooogh')

    
