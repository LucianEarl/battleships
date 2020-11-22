# Simulation Test
# By lucian
# 28/11/2019

from Simulation import Simulation

sim = Simulation()
# sim.process_command()  # test it processes commands properly
# sim.show_sea()  # test the map function works

# test the space checker
print(sim.occupied_space)  # check the occupied list before we update it
sim.check_space()  # run the space checker function
print(sim.occupied_space)  # check the list now the function has been run

"""Test Assertions:

process_command() tests

What would you like to do?:
show ships

Ships at sea:
Ship at [0 , 0   1 , 0   2 , 0   ]
Ship at [3 , 1   3 , 2   3 , 3   ]

What would you like to do?:
map
4 .  .  .  .  .

3 .  .  .  #  .

2 .  .  .  #  .

1 .  .  .  #  .

0 #  #  #  .  .

  0  1  2  3  4

What would you like to do?:
hug me
Please enter a valid command.

What would you like to do?:
place v,1,1
# no output

What would you like to do?:
exit battleships
# no output


show_sea() test

4 .  .  .  .  .

3 .  .  .  #  .

2 .  .  .  #  .

1 .  .  .  #  .

0 #  #  #  .  .

  0  1  2  3  4


check_space() test

[]
[(0, 0), (1, 0), (2, 0), (3, 1), (3, 2), (3, 3)]

"""