from math import hypot

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def get_distance(self, point: 'Point') -> float:
        """ Returns the distance between the person and the point """
        return hypot(self.x - point.x, self.y - point.y)

class IzolationZone(Point):
    def __init__(self, x: int, y: int, name: str):
        super().__init__(x, y)
        self.name = name

    def __repr__(self):
        return f"IzolationZone({self.x}, {self.y}, {self.name})"
