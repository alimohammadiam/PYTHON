
class Rectangle:
    def __init__(self, length: float, width: float) -> None:
        self.length = length
        self.width = width

    def __str__(self):
        return f'Rectangle, width: {self.width}, length: {self.width}'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.length!r}, {self.width!r})'

    def area(self) -> float:
        a = self.width * self.length
        return a

    def perimeter(self) -> float:
        p = 2 * (self.width + self.length)
        return p


class Car:
    def __init__(self, brand: str, model: str, year: str) -> None:
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self):
        return f'{self.brand} _ {self.model} _ {self.year}'

    def display(self) -> None:
        print(f'name: {self.brand}\nmodel: {self.model}\nyear of production: {self.year}')


class Student:
    """
    error management
    """

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.scores = dict()

    def __str__(self):
        return f'{self.name} _ {self.age}'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name}, {self.age})'

    def add_lesson(self) -> None:
        while True:
            print(f'add a lesson for add to ({self.name}) Student')
            print(f'press Exit to Exit')
            print(self.scores.items())
            l = input('>>> ')
            if l == 'E' or l == 'Exit':
                break
            self.scores[l] = 0

    def remove_lesson(self) -> None:
        while True:
            print(f'select lessons name to remove ({self.name} Student)')
            print(f'press Exit to Exit')
            print(self.scores)
            l = input('>>>')
            if l == 'E' or l == 'Exit':
                break
            del self.scores[l]

    def add_score(self) -> None:
        while True:
            print(f'select lesson to add acore')
            print(f'press Exit to Exit')
            print(self.scores.items())
            l = input(f'lesson >>> ')
            if l == 'E' or l == 'Exit':
                break
            s = int(input(f'score >>>'))
            if l in self.scores.keys():
                self.scores[l] = s
            else:
                print(f'select a existing lesson')

    def avg(self) -> None:
        sum = 0
        for value in self.scores.values():
            sum += value
        average = sum / len(self.scores)
        print(f'average all lessons ({self.name}) is _{average}_')


# # LBYL -> Look before you leap
# def check_len(obj):
#     if '__len__' in dir(obj):
#         print(len(obj))
#     else:
#         print('sorry...')
#
#
# # EAFP -> it's easier to ask for forgiveness than permission
# def check_len_2(obj):
#     try:
#         print(len(obj))
#     except TypeError:
#         print('sorry...')


class Animal:
    def __init__(self, name: str, cheek: str) -> None:
        self.name = name
        self.cheek = cheek

    def __str__(self) -> str:
        return f'{self.name}, {self.cheek}'

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.name}, {self.cheek})'

    def make_sound(self) -> None:
        print(f'Generic Animal sound')


class Mammal(Animal):
    def __init__(self, name: str, cheek: str, legs: int) -> None:
        super().__init__(name, cheek)
        self.legs = legs

    def __str__(self) -> str:
        return f'{self.name}, {self.cheek}, {self.legs}'

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.name}, {self.cheek}, {self.legs})'

    def make_sound(self) -> None:
        print(f'Generic Mammal sound')


class Dog(Mammal):
    def __init__(self, name: str, cheek: str, legs: int, breed: str) -> None:
        super().__init__(name, cheek, legs)
        self.breed = breed

    def __str__(self) -> str:
        return f'{self.name}, {self.cheek}, {self.breed}'

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.name}, {self.cheek}, {self.legs}, {self.breed})'

    def make_sound(self) -> None:
        print('Woof !!')


def main():
    pass


if __name__ == '__main__':
    main()
