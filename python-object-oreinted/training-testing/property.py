class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return (self.radius ** 2) * 3.14

    @area.setter
    def area(self, radius):
        if radius <= 0:
            raise ValueError('radius muss gt 0')
        self.radius = radius


class Temperature:
    def __init__(self, temp):
        self.temp = temp

    @property
    def fahrenheit(self):
        return self.fahrenheit * 1.8 + 32
