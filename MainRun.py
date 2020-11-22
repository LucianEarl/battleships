# Main
# By Lucian
# 27/11/2019


from Simulation import Simulation

sim = Simulation()


def welcome(): # show the welcome message and instructions
    print("\n\nWelcome to the Battleship game!\n"
            "By Lucian Earl and Prabhjot Singh.\n\n"
            "Type 'show ships' to show the current ships.\n"
            "type 'place <orientation>,<x>,<y>' to place a new ship.\n"
            "type 'map' to see the map.\n"
            "type 'exit battleships' to quit.\n")

welcome()
battleships_running = True  # the game is running by default

while battleships_running:
    sim.process_command()  # get the command from the user
    if sim.command.new_command == "exit battleships":  # if the command is to exit battleships, then stop loop
        battleships_running = False  # stop the game loop
