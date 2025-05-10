class Animal:
    def __init__(self, name: str, typ: str, **kwargs):
        self.name = name
        self.typ = typ

    def make_sound(self):
        print("Generic animal sound.")

    def __str__(self):
        return f'Animal: {self.name}'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name}, {self.typ})'


class Mammal(Animal):
    def __init__(self, legs: int, **kwargs):
        super().__init__(**kwargs)
        self.legs = legs

    def make_sound(self):
        print("Generic mammal sound.")

    def __str__(self):
        return f'Animal: {self.name}'

    def __repr__(self):
        return f'{self.__class__.__name__}(legs={self.legs}, name={self.name}, typ={self.typ})'


class Dog(Mammal):
    def __init__(self, breed: str, **kwargs):
        super().__init__(**kwargs)
        self.breed = breed

    def make_sound(self):
        print("Woof!")

    def __str__(self):
        return f'Animal: {self.name}'

    def __repr__(self):
        return f'{self.__class__.__name__}(name={self.name}, typ={self.typ}, legs={self.legs}, breed={self.breed})'
