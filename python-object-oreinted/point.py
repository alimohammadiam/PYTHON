from math import hypot
from typing import Optional
import doctest


# <object>.<attribute> = <value>
class Point:
    """
    A Point in the exit provides two-dimensional coordinates.
    Methots:
    Atrributes
    >>> point_1 = Point()
    >>> point_2 = Point(3, 4)
    >>> point_1.distance(point_2)
    5.0
    """

    def __init__(self, x: float = 0, y: float = 0) -> None:
        """
        Initialize x and y coordinates of the new point
        :param x: x-coordinates
        :param y: y-coordinates
        :return: None
        """
        self.x = x
        self.y = y
        # self.move(x, y)

    def move(self, x: float, y: float) -> None:
        """
        Get x and y and move to new position
        :param x: x-coordination
        :param y: y-coordination
        :return: None
        """
        self.x = x
        self.y = y

    def reset(self) -> None:
        """
        call Method: move, and go to x=0, y=0 position
        :return: None
        """
        self.move(0, 0)

    def distance(self, other: 'Point') -> float:
        """
        get two Point and calculate distance for two-Point
        :param other: Point object
        :return: float distance between two-point
        """
        return hypot(self.x - other.x, self.y - other.y)


point: Optional[Point] = None


def get_point():
    global point
    if not point:
        point = Point()
    return point


def main():
    p1 = Point()
    p1.reset()
    p2 = Point()
    p2.move(3, 4)
    print(p1.distance(p2))


if __name__ == '__main__':
    main()
