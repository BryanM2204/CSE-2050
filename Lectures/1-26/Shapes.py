class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def distance(self, other):
        'returns euclidean distance between two points'
        return ((self.x - other.x**2) + (self.y - other.y)**2) ** (1/2)

class Rectangle:
    def __init__(self, )