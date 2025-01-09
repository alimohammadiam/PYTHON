from math import hypot


class Point:

    def move(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def reset(self):
        self.move(0, 0)

    def distance(self, other: "Point"):
        return hypot(self.x - other.x, self.y - other.y)
