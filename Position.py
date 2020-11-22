# file name: Position
# author: Prabhjot
# date: 26/11/2019


class Position:

    def __init__(self, new_x, new_y):
        self.__x = new_x  # construct the x coordinate
        self.__y = new_y  # construct the y coordinate

    @property  # getter
    def x(self):
        return int(self.__x)

    @x.setter  # setter
    def x(self, value):
        self.__x = value

    @property  # getter
    def y(self):
        return int(self.__y)

    @y.setter  # setter
    def y(self, value):
        self.__y = value
