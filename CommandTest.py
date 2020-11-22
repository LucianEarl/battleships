# Command Test
# by Lucian
# 28/11/2019

from Command import Command
from Ship import Ship

command = Command()
command.get_command()

# test the success checker
print("The success check result is:", command.success_check)

# test the user command and error
if command.success_check:
    print("The user command result is:", command.new_command)
else:
    print("The error is:", command.error_message)

# test the ship placement checker
test_ships = [(0, 0), (1, 0), (2, 0)]  # we need some ships to test with

good_ship = Ship('h', (0,4))  # this ship should work
out_of_bounds = Ship('v', (100,100))  # this ship is out of bounds
overlapping = Ship('h', (0,0))  # this ship is on top of an existing ship

print("\nOut of bounds ship:")
if not command.check(test_ships, out_of_bounds):  # test out of bounds
    print("The error is:", command.error_message)
else:
    print("It worked.")

print("\nOverlapping ship:")
if not command.check(test_ships, overlapping):  # test out of bounds
    print("The error is:", command.error_message)
else:
    print("It worked.")

print("\nPerfect ship:")
if not command.check(test_ships, good_ship):  # test out of bounds
    print("The error is:", command.error_message)
else:
    print("It worked.")

"""Test Assertions:

get_command:

What would you like to do?:
exit battleships
The success check result is: True
The user command result is: exit battleships

What would you like to do?:
map
The success check result is: True
The user command result is: map

What would you like to do?:
show ships
The success check result is: True
The user command result is: show ships

What would you like to do?:
place v,1,1
The success check result is: True
The user command result is: place v,1,1

What would you like to do?:
place z,1,1
The success check result is: False
The error is: The orientation must be 'v' or 'h', followed by an x and y coordinate.

What would you like to do?:
place v,1,1,1,1
The success check result is: False
The error is: The orientation must be 'v' or 'h', followed by an x and y coordinate.

What would you like to do?:
place v,s,z
The success check result is: False
The error is: The orientation must be 'v' or 'h', followed by an x and y coordinate.

check()

Out of bounds ship:
The error is: The new ship will be out of bounds.

Overlapping ship:
The error is: There is already a ship in the way of the new ship.

Perfect ship:
It worked.
"""