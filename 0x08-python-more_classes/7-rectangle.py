#!/usr/bin/python3

"""Defines a Rectangle class."""

class Rectangle:
    """Represent a  rectangle."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Constructor method"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """Destructor method"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """Getter method for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Method that returns the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Method that returns the perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Method that returns a string representation of the rectangle"""
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join([str(self.print_symbol) * self.width] * self.height)

    def __repr__(self):
        """Method that returns a string representation of the rectangle that can be used to recreate it"""
        return f"Rectangle({self.width}, {self.height})"

