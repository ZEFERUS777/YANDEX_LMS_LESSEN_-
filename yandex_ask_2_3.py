class Point:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.cord = tuple((x, y))

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def __str__(self):
        return f'{self.name}{tuple((self.x, self.y))}'

    def invert(self):
        return Point(self.name, self.y, self.x)

    def __invert__(self):
        return self.invert()

    def get_coords(self):
        return tuple((self.x, self.y))
