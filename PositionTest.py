# Position Test
# By Lucian and Prabhjot
# 26/11/2019

from Position import Position

position_1 = Position(4,3)
position_2 = Position(0,0)

print("Position 1 x:", position_1.x, "y:", position_1.y)  # test the getters
print("Position 2 x:", position_2.x, "y:", position_2.y)

position_1.x = 7  # test the getters
position_1.y = 0

print("Position 1 x:", position_1.x, "y:", position_1.y)

"""Test Assertion
Position 1 x: 4 y: 3
Position 2 x: 0 y: 0
Position 1 x: 7 y: 0
"""