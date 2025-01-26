import math

class Shape:
    """Base class for shapes."""
    def area(self):
        raise NotImplementedError("The area method must be overridden by the subclass.")

class Rectangle(Shape):
    """Rectangle class inheriting from Shape."""
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    """Circle class inheriting from Shape."""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2
