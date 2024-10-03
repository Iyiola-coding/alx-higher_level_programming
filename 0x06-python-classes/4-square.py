#!/usr/bin/python3
""" Define a Square class """


class Square:
    """ representation of a Square class """

    def __init__(self, size=0):
        """ instantation with size for our object initialization """
        self.__size = size

        """ The getter for the private attr size """
    @property
    def size(self):
        """ property getter """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ A method that returns the current square area """
        return (self.__size * self.__size)
