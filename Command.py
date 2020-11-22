# Command
# By Lucian and Prabhjot
# 27/11/2019

from Ship import Ship


class Command:

    def __init__(self):
        self.__new_command = str  # new command has to start as something
        self.__success_check = False  # start the success as false so nothing gets through
        self.__error_message = "Please enter a valid command." # this is the first error

    @property # getter
    def new_command(self):
        return self.__new_command

    @new_command.setter  # setter
    def new_command(self, value):
        self.__new_command = value

    @property # getter
    def error_message(self):
        return self.__error_message

    @error_message.setter  # setter
    def error_message(self, value):
        self.__error_message = value

    @property # getter
    def success_check(self):
        return self.__success_check

    @success_check.setter  # setter
    def success_check(self, value):
        self.__success_check = value

    def get_command(self):  # this function checks that the command is valid
        self.error_message = "Please enter a valid command."
        self.success_check = False
        # set  back to default  in case they were changed

        user_input = input("\nWhat would you like to do?:\n").lower()

        if user_input[:5] == "place":  # if the user entered place
            place_command = user_input[6:].split(',')  # split the other arguments into a list for ease
            # check the first argument is v or h, and that there are two numeric coordinates
            if len(place_command) == 3 and (place_command[0] == "h" or place_command[0] == "v")\
                    and (place_command[1].isnumeric() and place_command[2].isnumeric()):
                self.new_command = user_input
                self.success_check = True
            else:
                self.error_message = "The orientation must be 'v' or 'h', followed by an x and y coordinate."

        elif user_input == "show ships" or user_input == "map" or user_input == "exit battleships":
            # check other commands with no arguments
            self.new_command = user_input
            self.success_check = True

    def check(self, ships, new_ship):
        # this function checks if the new ship is within bounds and not overlapping an existing ship

        for i in range(0, 3):  # check that it is not out of bounds. Max is 4, min is 0.
            if new_ship.ship_position[i].x > 4 or new_ship.ship_position[i].y > 4\
                    or new_ship.ship_position[i].x < 0 or new_ship.ship_position[i].y < 0:
                self.error_message = "The new ship will be out of bounds.\n"
                return False

        for i in range(0, 3):  # for each piece of the new ship, check if it matches any other ship pieces
            if (new_ship.ship_position[i].x, new_ship.ship_position[i].y) in ships:
                self.error_message = "There is already a ship in the way of the new ship.\n"
                return False
        # if it get to here, the ship is in a valid position
        return True

