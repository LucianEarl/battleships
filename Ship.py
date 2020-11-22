# Ship
# By Lucian and Prabhjot
# 26/11/2019

from Position import Position


class Ship:
    def __init__(self, user_orientation, initial_position):
        if user_orientation == "h": # if the orientation is horizontal, then the x coordinate increases
            self.__ship_position = [Position(initial_position[0], initial_position[1]),
                                    Position(int(initial_position[0]) + 1, initial_position[1]),
                                    Position(int(initial_position[0]) + 2, initial_position[1])]
        else:  # if the orientation is vertical, then the y coordinate increases
            self.__ship_position = [Position(initial_position[0], initial_position[1]),
                                    Position(initial_position[0], int(initial_position[1]) + 1),
                                    Position(initial_position[0], int(initial_position[1]) + 2)]
        self.__orientation = user_orientation

    @property # getter
    def ship_position(self):
        return self.__ship_position

    @property # getter
    def orientation(self):
        return self.__orientation

    #  setters are not needed, as the values are set in construction and the ship will never move
