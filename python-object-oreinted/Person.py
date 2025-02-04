class Person:
    def __init__(self, first_name: str, last_name: str, age: int):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def __repr__(self):
        return f'{self.__class__.__name__}("{self.first_name}", "{self.last_name}", "{self.age}")'


def main():
    pass


if __name__ == '__main__':
    main()
