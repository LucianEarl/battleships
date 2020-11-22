# Ship Test
# By Lucian and Prabhjot
# 27/11/2019

from Ship import Ship

ship_1 = Ship("h", (0, 0))
print("\nShip 1 Position:")
for position in ship_1.ship_position:
    print("X:", position.x, "Y:", position.y)
print("Orientation:", ship_1.orientation)

ship_2 = Ship("v", (3, 1))
print("\n\nShip 2 Position:")
for i in ship_2.ship_position:
    print("X:", i.x, "Y:", i.y)
print("Orientation:", ship_2.orientation)


"""Test Assertion:
Ship 1 Position:
X: 0 Y: 0
X: 1 Y: 0
X: 2 Y: 0
Orientation: h


Ship 2 Position:
X: 3 Y: 1
X: 3 Y: 2
X: 3 Y: 3
Orientation: v
"""