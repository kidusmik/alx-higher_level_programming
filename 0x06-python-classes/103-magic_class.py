#!/usr/bin/python3
"""Definition of MagicClass class that does exactly the same as a
Python bytecode given in the task.
"""
import math


class MagicClass:
    """Defines a class MagicClass.

    Attributes:
        __radius: radius of the circle

    Args:
        radius: radius of the circle
    """
    def __init__(self, radius=0):
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Calculates the area of the circle."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Calculates the circumference of the circle."""
        return (2 * math.pi * self.__radius)
