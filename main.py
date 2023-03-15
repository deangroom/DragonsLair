import json
import random
import time

# import create_grid from game_map.py
from game_map import create_grid

#create typing effect
def typing_effect(text):
    for char in text:
        time.sleep(0.02)
        print(char, end='', flush=True)

#Create a random line of text from stupid.md using random.choice and typing effect
def random_line():
    with open("stupid.md", "r") as f:
        lines = f.readlines()
        random_line = random.choice(lines)
        typing_effect(random_line)



# create a loading effect
def loading_effect(text):
    # clear the screen
    print("\033c", end='')
    for char in text:
        time.sleep(0.1)
        print(char, end='', flush=True)

def load_game():
    # load the grid_data from the json file
    with open("game_data.json", "r") as f:
        grid_data = json.load(f)
    return grid_data

# create a function to print the grid_data as a table
def print_grid_data(grid_data):
    for row in grid_data:
        print(row, grid_data[row])
    print()
    
# create a function to start the game
def start_game():
    # use typing effect to tell the player to press B to begin
    typing_effect("\nType B to begin and press enter > ")
    # create a while loop to check if the player has pressed B
    while True:
        # get the player's input
        player_input = input()
        # if the player has pressed B, break the loop
        if player_input == "b" or "B":
            # clear the screen
            print("\033c", end='')
            break
        # if the player has not pressed B, tell them to press B
        else:
            typing_effect("It's not hard. Press B to begin")

#------------------LOADER------------------#

# create a loading function
def game_loader():
    load_game()
    time.sleep(1)
    print("\033c", end='') # clear the screen

    typing_effect("Welcome to Dragon's Lair - Insert Coins")
    time.sleep(2)
    print("\033c", end='')
    typing_effect("Just kidding, this game is free, the cake is a lie")
    time.sleep(1)
    print("\033c", end='') # clear the screen

    #load the welcome screen text from loader.md file
    with open("loader.md", "r") as f:
        loader = f.read()
        typing_effect(loader)



#------------------MAIN------------------#

#create the grid
grid = create_grid()



#load the game
game_loader()

#start the game
start_game()

#------------------START------------------#

#clear the screen
print("\033c", end='')

# set player coordinates
player_coordinates = (0, 0)

# set the exit coordinates
exit_coordinates = (5, 5)

# if player coordinates are not the same as exit coordinates, keep playing
while player_coordinates != exit_coordinates:
    #print the players current location, title and narrative
    typing_effect(grid[player_coordinates[0]][player_coordinates[1]]["title"])
    print()
    typing_effect(grid[player_coordinates[0]][player_coordinates[1]]["narrative"])

    #check if the player is in the same room as a monster
    if "M" in grid[player_coordinates[0]][player_coordinates[1]]:
        #print the monster's name
        print("You have encountered a", grid[player_coordinates[0]][player_coordinates[1]]["M"]["name"])
    
    #check if the player is in the same room as daphne
    if "D" in grid[player_coordinates[0]][player_coordinates[1]]:
        #print the monster's name
        print("You have encountered Daphne")
        # break the loop
        break

    # get movement, left, right, forward and back using the input function for W, A, S, D
   
    movement = input("\nUse W, A, S, D to move > ")

    # if the player presses W and X is not 0, move the player up
    if movement == "w" and player_coordinates[0] != 0:
        player_coordinates = (player_coordinates[0] - 1, player_coordinates[1])
    # if the player presses A and Y is not 0, move the player left
    elif movement == "a" and player_coordinates[1] != 0:
        player_coordinates = (player_coordinates[0], player_coordinates[1] - 1)
    # if the player presses S and X is not 5, move the player down
    elif movement == "s" and player_coordinates[0] != 5:
        player_coordinates = (player_coordinates[0] + 1, player_coordinates[1])
    # if the player presses D and Y is not 5, move the player right
    elif movement == "d" and player_coordinates[1] != 5:
        player_coordinates = (player_coordinates[0], player_coordinates[1] + 1)
    # if the player presses W and X is 0, tell them they can't move
    elif movement == "w" and player_coordinates[0] == 0:
        print("You can't go that way")
    # if the player presses A and Y is 0, tell them they can't move
    elif movement == "a" and player_coordinates[1] == 0:
        print("You can't go that way")
    # if the player presses S and X is 5, tell them they can't move
    elif movement == "s" and player_coordinates[0] == 5:
        print("You can't go that way")
    # if the player presses D and Y is 5, tell them they can't move
    elif movement == "d" and player_coordinates[1] == 5:
        print("You can't go that way")
    # if the player presses anything else, tell them they can't move
    else:
        print("You can't go that way - serusly, use W, A, S, D")
    
    # clear the screen
    print("\033c", end='')
    random_line()
    print()
    



#------------------END------------------#



