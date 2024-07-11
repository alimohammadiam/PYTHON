from pprint import pprint


class Rectangle:
    """
    It takes the length and width of the rectangle and calculates the perimeter and area of the rectangle

    """
    all_rectangle: list["Rectangle"] = []

    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        Rectangle.all_rectangle.append(self)

    def __str__(self) -> str:
        return (f"Rectangle with number {Rectangle.all_rectangle.index(self) + 1}--> width: {self.width}."
                f" height: {self.height} ")

    def __repr__(self) -> str:
        return f"{__class__.__name__}({self.width!r}, {self.height!r})"

    def display(self) -> None:
        """
        Show all the Rectangle
        :return:
        """
        pprint(self.__str__())

    def area(self) -> int:
        """
        Calculate the area of the rectangle
        :return:
        """
        a = self.height * self.width
        return a

    def environment(self):
        """
        Calculate the perimeter of the rectangle
        :return:
        """
        e = 2 * (self.width + self.height)
        return e


class Car:
    """
    information of Cars --> brand, model, year
    """
    all_car: list["Car"] = []

    def __init__(self, name: str, brand: str, model: str, year: str) -> None:
        self.name = name
        self.brand = brand
        self.model = model
        self.year = year
        Car.all_car.append(self)

    def __str__(self) -> str:
        return f"Car: {self.name} / {self.brand}"

    def display(self) -> str:
        """
        Show information of Car
        :return:
        """
        return (f"Car information:\n name:{self.name}\n company: {self.brand}\n model: {self.model}\n"
                f" year: {self.year}")


class Student:
    # do not test yet !
    def __init__(self, name: str, age: int, scores: dict = {}) -> None:
        self.scores = {}
        self.name = name
        self.age = age

    def __str__(self):
        return f"Student: {self.name}"

    def __repr__(self):
        return f"{__class__.__name__}( {self.name} / {self.age} / lesson: {self.scores.keys()})"

    def set_score(self):
        lesson_score = {}
        while True:
            choice = int(input(f"({self.name})enter 0 for exit / enter 1 for (Enter scores: )"))
            if choice == 1:
                lesson = input("name lesson: ", )
                score = int(input("score of {} is :".format(lesson)))
                if 0 <= score <= 20:
                    lesson_score[lesson] = score
                    self.scores[lesson] = score
                else:
                    print("invalid score !")
            elif choice == 0:
                break
            else:
                print("Please enter a valid choice (0/1) !")

    def set_avg(self):
        avg, sum = 0, 0
        for i in self.scores.keys():
            sum += self.scores[i]
        if len(self.scores) != 0:
            avg = sum / len(self.scores)
            return avg

    def display(self):
        return f"{self.name}: {self.age} years old / lesson: {self.scores.items()} / avg: {Student.set_avg(self)}"


def main():
    pass
    # for class ( Student )
    # ali = Student("ali", 24)
    # reza = Student("reza", 25)
    # ali.set_score()
    # reza.set_score()
    # print(ali.__str__())
    # print(40 * "*")
    # print(ali.__repr__())
    # print(40 * "*")
    # print(ali.display())
    # print(40 * "*")
    # print(reza.__str__())
    # print(40 * "*")
    # print(reza.__repr__())
    # print(40 * "*")
    # print(reza.display())


if __name__ == "__main__":
    main()
