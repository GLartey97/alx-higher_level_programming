#!/usr/bin/python3
"""Define a class Rectangle"""


class Rectangle:
    """Represent a rectangle."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializing a new rectangle.
        Args:
            width (int): The width of the new rectangle
            height (int): The height of the new rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        rectangle = []
        for i in range(self.height):
            rectangle.append(str(self.print_symbol) * self.width)
        return "\n".join(rectangle)

    def __repr__(self):
        return f"Rectangle({self._width}, {self._height})"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
