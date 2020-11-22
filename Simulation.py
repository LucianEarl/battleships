# Simulation
# by Lucian and Prabhjot
# 27/11/2019

from Command import Command
from Ship import Ship


class Simulation:
    def __init__(self):
        self.__command = Command()  # create the command object for processing commands
        self.__ship_1 = Ship("h", (0, 0))  # create the initial two ships
        self.__ship_2 = Ship("v", (3, 1))
        self.__ship_list = [self.__ship_1,self.__ship_2]  # create a list to keep track of ships
        self.__sea_row = [" 0 ", " 0 ", " 0 ", " 0 ", " 0 "]  # easier to repeat this 5 times than type it all
        self.__sea = [self.__sea_row, self.__sea_row, self.__sea_row, self.__sea_row, self.__sea_row]
        self.__occupied_space = []  # no space occupied yet

    @property  # getter
    def command(self):
        return self.__command

    @property  # getter
    def sea(self):
        return self.__sea

    @property  # getter
    def ship_list(self):
        return self.__ship_list

    @ship_list.setter # setter
    def ship_list(self, value):
        self.__ship_list = value

    @property  # getter
    def ship_1(self):
        return self.__ship_1

    @property  # getter
    def ship_2(self):
        return self.__ship_2

    @property  # getter
    def occupied_space(self):
        return self.__occupied_space

    @occupied_space.setter # setter
    def occupied_space(self, value):
        self.__occupied_space = value

    def process_command(self):
        self.check_space()  # run this here to update the list of occupied spaces in case a new one was placed
        self.command.get_command()  # get the user command

        # now check the success_check property
        if self.command.success_check:
            # use if elif to execute the appropriate ship methods
            if self.command.new_command == "show ships":
                print("\nShips at sea:")

                for ship in self.ship_list:  # check each ship in the list
                    print("Ship at [", end='')
                    for coord in ship.ship_position:  # for each of the three ship segments
                        print(coord.x, ",", coord.y, end='   ')  # print the x and y coordinates
                    print("]")

            elif self.command.new_command[:5] == "place":  # if this is a place command
                place_command = self.command.new_command.lower()[6:].split(',')  # split the arguments into a list
                new_ship = Ship(place_command[0], [place_command[int(1)], place_command[int(2)]])  # create a new ship
                if self.command.check(self.occupied_space, new_ship):  # use the check function to see if free space
                    self.ship_list.append(new_ship)  # add the ship to the list if it passes
                else:
                    print(self.command.error_message)  # otherwise print an error

            elif self.command.new_command == "map":
                self.show_sea() # show the current sea board
        else:  # the user entered an invalid statement
            print(self.command.error_message)

    def check_space(self):
        # create a list of spaces where ships are
        for ship in self.ship_list:  # for each ship in the list
            for piece in ship.ship_position:  # for each piece of the ship
                self.occupied_space.append((piece.x, piece.y))  # add that coordinate to the list

    def show_sea(self):
        # this function shows every position on the sea, and whether there is a ship there or not

        for y_coord in range(4, -1, -1):  # done in reverse, as that is how coordinate grids are shown
            print(y_coord, end="")  # show the y axis label, and don't start a new line
            for x_coord in range(0, 5):
                if (x_coord, y_coord) in self.occupied_space:  # check if the current coordinate is occupied
                    print(" # ",end="")  # use the # symbol for a ship
                else:  # if it is unoccupied
                    print(" . ",end="")  # use the . symbol for empty space
            print("\n")  # finished one row, start a new line for the next
        print("  0  1  2  3  4")  # x axis labels
