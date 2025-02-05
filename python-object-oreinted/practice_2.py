from pprint import pprint

class Rectangle:
    """
    Create Rectangle Object and Calculate its perimeter and environment
    """
    all_rectangles: list["Rectangle"] = []

    def __init__(self, width: float, length: float, height: float = 0) -> None:
        self.width = width
        self.length = length
        self.height = height
        Rectangle.all_rectangles.append(self)

    def __str__(self) -> str:
        return f'Rectangle number of {Rectangle.all_rectangles.index(self) + 1}: width: {self.width}, length: {self.length}'

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.width!r}, {self.length!r}, {self.height!r})'

    def display(self) -> None:
        """
        Show info about Rectangle
        :return:
        """
        pprint(self.__str__())

    def perimeter(self) -> float:
        """
        Calculate perimeter of Rectangle
        :return: flout -> perimeter
        """
        perimeter = (self.width + self.length) * 2
        return perimeter

    def environment(self) -> float:
        """
        Calculate environment of Rectangle
        :return: flout -> environment
        """
        environment = (self.width * self.length)
        return environment

    def help_perimeter(self) -> None:
        """
        It shows and explains the steps of perimeter calculation
        :return: None -> print in Method
        """
        print(f'Rectangle Perimeter: \n\t\tperimeter = 2 * (width + length)')
        print(f'\nIn your Rectangle: \n\t\t_ {self.perimeter()} _ = 2 * ({self.width} + {self.length})')

    def help_environment(self) -> None:
        """
        It shows and explains the steps of environment calculation
        :return: None -> print in Method
        """
        print(f'Rectangle environment: \n\t\tenvironment = width * length')
        print(f'In your Rectangle: \n\t\t_ {self.environment()} _ = {self.width} * {self.length}')


class Car:
    """
    information of Cars --> brand, model, year
    """
    all_car: list["Car"] = []

    def __init__(self, name: str, brand: str, model: str, age: str):
        self.name = name
        self.brand = brand
        self.model = model
        self.age = age
        Car.all_car.append(self)

    def __str__(self) -> str:
        return f'{self.name}/ Year {self.age}/ {self.brand}'

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.name!r}, {self.brand!r}, {self.model!r}, {self.age!r})'

    def display(self) -> str:
        """
        Show information of Car
        :return:
        """
        return (f"Car information: \n name: {self.name}\n company: {self.brand}\n model: {self.model}\n"
                f" year: {self.age}")


class Student:
    pass


def main():
    pass


if __name__ == '__main__':
    main()
