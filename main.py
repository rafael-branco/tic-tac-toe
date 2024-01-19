
def check_win(grid):
    # player is 'X' or 'O'
    players = ['X', 'O']
    for player in players:
        if grid[0][0] == player and grid[0][1] == player and grid[0][2] == player:
            return player
        elif grid[1][0] == player and grid[1][1] == player and grid[1][2] == player:
            return player
        elif grid[2][0] == player and grid[2][1] == player and grid[2][2] == player:
            return player
        elif grid[0][0] == player and grid[1][0] == player and grid[2][0] == player:
            return player
        elif grid[0][1] == player and grid[1][1] == player and grid[2][1] == player:
            return player
        elif grid[0][2] == player and grid[1][2] == player and grid[2][2] == player:
            return player
        elif grid[0][0] == player and grid[1][1] == player and grid[2][2] == player:
            return player
        elif grid[0][2] == player and grid[1][1] == player and grid[2][0] == player:
            return player

    return False

def fill_box(grid, player, row, column):
    if grid[row][column] == ' ':
        grid[row][column] = player
    else:
        print("This box is already filled!")

grid = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]



print(check_win(grid))


