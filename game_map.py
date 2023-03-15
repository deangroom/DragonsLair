import json
import random
# load the room descriptions from the md file into a dictionary
def load_room_data():
    with open("room_narrative.md", "r", encoding="utf-8") as f:
        data = f.read().split("#")[1:]
    
    return {title.strip(): narrative.strip() for title, narrative in [d.split(":") for d in data]}

def create_grid():
    """Create a 6x6 grid representing the game map."""
    # fetching room dict only once for all iterations
    room_narrative_dict = load_room_data()

    grid_data = {}
    for row in range(6):
        grid_data[row] = {}
        for column in range(6):
            # populating the grid with their respective room info
            room_title = random.choice(list(room_narrative_dict.keys()))
            grid_data[row][column] = {
                "title": room_title,
                "coordinates": (row, column),
                "narrative": room_narrative_dict[room_title]
            }
    # add the player to the grid
    grid_data[0][0]["P"] = True
    # add the exit to the grid
    grid_data[5][5]["E"] = True

    # save the grid_data to a json file
    with open("game_data.json", "w") as f:
        json.dump(grid_data, f)
    return grid_data

# create a list of monsters with random hitpoints
def create_monsters():
    monsters = [
        {"name": "Rat King", "hitpoints": random.randint(1, 10)},
        {"name": "Rick Astley", "hitpoints": random.randint(1, 10)},
        {"name": "Undead Guard", "hitpoints": random.randint(1, 10)},
        {"name": "Dragon", "hitpoints": random.randint(1, 10)},
    ]
    return monsters

# place the monsters in random rooms
def place_monsters(grid):
    monsters = create_monsters()
    for monster in monsters:
        monster["coordinates"] = (random.randint(0, 5), random.randint(0, 5))
        grid[monster["coordinates"][0]][monster["coordinates"][1]]["M"] = monster
    return grid

# put Daphne in a random room
def place_daphne(grid):
    daphne = {"name": "Daphne", "hitpoints": random.randint(1, 10)}
    daphne["coordinates"] = (random.randint(0, 5), random.randint(0, 5))
    grid[daphne["coordinates"][0]][daphne["coordinates"][1]]["D"] = daphne
    return grid

# print where the player it
def print_player_location(grid):
    for row in grid:
        for column in grid[row]:
            if "P" in grid[row][column]:
                print(f"You are in the {grid[row][column]['title']}")
    return grid

# print where daphne is
def print_daphne_location(grid):
    for row in grid:
        for column in grid[row]:
            if "D" in grid[row][column]:
                print(f"Daphne is in the {grid[row][column]['title']}")
    return grid

# print where the monsters are
def print_monster_location(grid):
    for row in grid:
        for column in grid[row]:    
            if "M" in grid[row][column]:
                print(f"There is a {grid[row][column]['M']['name']} in the {grid[row][column]['title']}")
    return grid






