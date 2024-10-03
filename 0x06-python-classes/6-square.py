#!/usr/bin/python3
""" Define a Square class """


class Square:
    """ representation of a Square class """

    position: def __init__(self, size=0, position=(0, 0)):
        """ initiate a new created square
        where: size equates the square and given a default value 0
        position is a tuple"""
        self.__size = size
        self.__position = position

        """ private attribute """
        @property
        def positions(self):
            """ property getter """
            return self.__size

        @size.setter
        def size(self, value):
            """ to make the set value meet standard """
        if not isinstance(value, int):
            raise TypeError
        elif value < 0:
            raise ValueError
        self.__value

         @property
        def positions(self):
            """ property getter """
            return self.__position

        @position.setter
        def position(self, value):
            """ to make the set value meet standard """
            if (not isinstance(value, tuple) or
            len(value) !=2 or
            not all(isinstance(num, int) for num in value) or
            not all(num >=0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integer")

    @position.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ A method that returns the current square area """
        return (self.__size * self.__size)

    def my_print(self):
        """ print rep of square with # character """
        if self.__size == 0:
            print()
        for item in range(self.__size):
            [print("#", end="") for j in range(self.__size)]
            print()
