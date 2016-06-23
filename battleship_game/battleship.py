import copy

# creating an empty list to store a grid
grid = []

# creating an empty dictionary to store the ships
ships = {}

def new_game(grid_width, grid_height):
    # adding rows
    for i in range(grid_height):
        grid.append([])
        # adding columns with clear water mark '~' at each place
        for j in range(grid_width):
            grid[i].append("~")

def place_ship(player_name, x, y, direction):

    # for horizontal direction try to add a ship parts left and right from the central position
    if direction == "Horizontal":
        if grid[y][x-1] == "~" and grid[y][x+1] == "~":
            grid[y][x] = player_name
            grid[y][x-1] = player_name
            grid[y][x+1] = player_name
            if player_name not in ships:
                ships[player_name] = [[(x-1,y),(x,y),(x+1,y)]]
            else:
                ships[player_name].append([(x-1,y),(x,y),(x+1,y)])
        else:
            raise ValueError

    # for vertical direction try to add a ship parts up and down from the central position
    elif direction == "Vertical":
        if grid[y-1][x] == "~" and grid[y+1][x] == "~":
            grid[y][x] = player_name
            grid[y-1][x] = player_name
            grid[y+1][x] = player_name
            if player_name not in ships:
                ships[player_name] = [[(x,y-1),(x,y),(x,y+1)]]
            else:
                ships[player_name].append([(x,y-1),(x,y),(x,y+1)])
        else:
            raise ValueError

def fire(x,y):

    #fire is out of grid
    if x >= len(grid[0]) or y >= len(grid):
        print("Mate! you're out of bounds")

    else:
        # if the ship is not in the cell print miss and mark cell as missed with '.'
        if grid[y][x] == "~" or grid[y][x] == ".":
            print("Miss\n")
            grid[y][x] = "."

        # if the ship is in the cell print hit message and change the cell to hit symbol
        else:
            print("Hit!\n")
            player = grid[y][x]
            grid[y][x] = "!"
            for val in ships[player]:
                if (x,y) in val:
                    val.remove((x,y))

            # checking if ship if sunk
            for val in ships[player]:
                if len(val) == 0:
                    print(player + " lost a ship\n")
                    ships[player].remove(val)

            # checking if player who's ship got hit lost all the ships and if so declaring the winner
            if not any(player in row for row in grid):
                print(player + " is out of the game\n")

                # finding the name of the remaining player
                for row in grid:
                    for value in row:
                        if value != "~" and value != "." and value != "!":
                            winning_player = value
                            break

                # printing a winning message
                print(winning_player + " is the winner\n")

def print_grid(player_name):

    # making a deep copy of the grid, so that when we change player names to "#" for printing, it won't affect actual grid
    pr_grid = copy.deepcopy(grid)

    # finding a name of a player in grid
    for i in range(len(pr_grid)):
        for j in range(len(pr_grid[i])):
            if pr_grid[i][j] != "~" and pr_grid[i][j] != "." and pr_grid[i][j] != "!":

                # changing player name to "#"
                if pr_grid[i][j] == player_name:
                    pr_grid[i][j] = "#"

                # change other player name to ~ symbol
                else:
                    pr_grid[i][j] = "~"

    # printing the grid
    print ('()\n'.join(''.join(row) for row in pr_grid) + "()")
