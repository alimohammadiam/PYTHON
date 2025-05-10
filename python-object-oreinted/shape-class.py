class Shape:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.area = 0
        self.perimeter = 0

    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass

    def show(self):
        info = ''
        for key, value in self.__dict__.items():
            if value > 0:
                info += f'{key}: {value: .2f}\n'
        print(info)

    def __str__(self):
        return self.__class__.__name__


# length, width
class Rectangle(Shape):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def calculate_area(self):
        self.area = self.length * self.width

    def calculate_perimeter(self):
        self.perimeter = 2 * (self.length + self.width)


# length
class Square(Shape):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def calculate_area(self):
        self.area = self.length ** 2

    def calculate_perimeter(self):
        self.perimeter = self.length * 4


# base, height, side1, side2
class Triangle(Shape):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def calculate_area(self):
        self.area = (self.base * self.height) / 2

    def calculate_perimeter(self):
        self.perimeter = self.base + self.side1 + self.side2


# (لوزی) diameter1, diameter2, length
class Rhombus(Shape):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def calculate_area(self):
        self.area = (self.diameter1 * self.diameter2) / 2

    def calculate_perimeter(self):
        self.perimeter = self.length * 4


# (متوازی الاظلاع) length, width
class Parallelogram(Shape):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def calculate_area(self):
        self.area = self.length * self.width

    def calculate_perimeter(self):
        self.perimeter = (self.length + self.width)


# (ذوزنقه) base, top, height, side1, side2
class Trapezium(Shape):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def calculate_area(self):
        self.area = (self.top + self.base) * self.height * 1/2

    def calculate_perimeter(self):
        self.perimeter = self.top + self.base + self.side1 + self.side2


# radius
class Circle(Shape):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def calculate_area(self):
        self.area = self.radius ** 2 * 3.14

    def calculate_perimeter(self):
        self.perimeter = 2 * self.radius * 3.14


def main():
    rectangle = Rectangle(length=6, width=2)
    print(rectangle)
    rectangle.calculate_area()
    rectangle.calculate_perimeter()
    rectangle.show()
    print('_' * 40)

    square = Square(length=4)
    print(square)
    square.calculate_area()
    square.calculate_perimeter()
    square.show()
    print('_' * 40)

    triangle = Triangle(base=4, height=3, side1=3, side2=5)
    print(triangle)
    triangle.calculate_area()
    triangle.calculate_perimeter()
    triangle.show()
    print('_' * 40)

    rhombus = Rhombus(diameter1=6, diameter2=10, length=6)
    print(rhombus)
    rhombus.calculate_area()
    rhombus.calculate_perimeter()
    rhombus.show()
    print('_' * 40)

    parallelogram = Parallelogram(length=6, width=2, height=2)
    print(parallelogram)
    parallelogram.calculate_area()
    parallelogram.calculate_perimeter()
    parallelogram.show()
    print('_' * 40)

    trapezium = Trapezium(height=4, base=8, top=5, side1=4, side2=6)
    print(trapezium)
    trapezium.calculate_area()
    trapezium.calculate_perimeter()
    trapezium.show()
    print('_' * 40)

    circle = Circle(radius=4)
    print(circle)
    circle.calculate_area()
    circle.calculate_perimeter()
    circle.show()
    print('_' * 40)


if __name__ == '__main__':
    main()
