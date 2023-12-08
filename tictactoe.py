import random

# Initialize the method of data storing using a list that will use 
# nested lists to store data; while also leaving space (" ") to place 
# objects (user/computer choice)
grid = [[" " for _ in range(3)] for _ in range(3)]

# Function will print grid in terminal with "|" and "-" for every sub list within main 
# grid list to visibly separate (user/computer choices)
def print_grid():
    for row in grid:
        print(" | ".join(row))
        print("-" * 9)

def clear_grid():
    for i in range(0, 3):
        for x in range(0, 3):
            grid[i][x] = " "
"""
Will be using lists as a way of storing user/computer data
to later down the code, change the value of grid[i] to put in a 
particular value that user wishes to put in to fulfill the check_win() function.
"""

# Function that'll randomly place its option into grid while checking if that 
# spot is already taken, it'll redo it again. 
def computer_move_easy(playerTwo):
    while True: 
            row = random.randint(0, 2) # Will try putting in row from [0,2]
            column = random.randint(0, 2) # Will try putting in colum from [0,2]
            if grid[row][column] == " ":
                grid[row][column] = playerTwo
                break

def computer_move_normal(playerTwo):
        # Row 0:
        if grid[0][0] == grid[0][1] and grid[0][0] != " " and grid[0][2] == " ": # Places symbol on grid[0][2]
            grid[0][2] = playerTwo
            return
        
        computer_move_easy(playerTwo)
        return

# Function for a player's turn
def player_turn(player):
    while True:
        try:
            row = int(input(f"Player {player}, enter the row (0, 1, 2): "))
            col = int(input(f"Player {player}, enter the column (0, 1, 2): "))
            if 0 <= row < 3 and 0 <= col < 3 and grid[row][col] == " ": # Checks validity of users choice
                grid[row][col] = playerOne if player == 1 else playerTwo
                break
            else:
                print("Invalid input. Try again.")
        except ValueError:
            print("Invalid input. Try again.")

# Function to check for a win or draw
def check_win():
    for row in grid:
        if row[0] == row[1] == row[2] != " ":
            return True
    for col in range(3):
        if grid[0][col] == grid[1][col] == grid[2][col] != " ":
            return True
    if grid[0][0] == grid[1][1] == grid[2][2] != " ":  # Top-left to the bottom-right diagonal
        return True
    if grid[0][2] == grid[1][1] == grid[2][0] != " ":  # Top-right to the bottom-left diagonal
        return True
    
    # Checks for a draw within the grid
    if all(grid[i][j] != " " for i in range(3) for j in range(3)):
        return "Draw"
    return False

#make the choice outisde and just have an if statement that leads into 2 while loops
def main():
    if playerOne == 'X':
        playerTwo = 'O'
        current_player = 1
    elif playerOne == 'O':
        playerTwo = 'X'
        current_player = 2
    if choice == "Player":
        while True:
            print_grid()
            player_turn(current_player)
            result = check_win()
            if result == "Draw":
                print_grid()
                print("It's a draw!")
                break
            elif result:
                print_grid()
                print(f"Player {current_player} wins!")
                break
            current_player = 3 - current_player

    elif choice == "Computer":
        if difficulty == "easy":
            while True:
                if current_player == 1:  # Player's turn
                    print_grid()
                    player_turn(1)
                else:  # Computer's turn
                    computer_move_easy(playerTwo)
                result = check_win()
                if result == "Draw":
                    print_grid()
                    print("It's a draw!")
                    break
                elif result:
                    print_grid()
                    print(f'Player {current_player} wins!')
                    break
                current_player = 3 - current_player
        elif difficulty == "normal": 
            while True:
                if current_player == 1:  # Player's turn
                    print_grid()
                    player_turn(1)
                else:  # Computer's turn
                    computer_move_normal(playerTwo)
                result = check_win()
                if result == "Draw":
                    print_grid()
                    print("It's a draw!")
                    break
                elif result:
                    print_grid()
                    print(f'Player {current_player} wins!')
                    break
                current_player = 3 - current_player

# Main game loop that will set game forward
while True:
    choice = input("Who would you like to play against(Computer or Player?)")
    if choice == "Player":
        # Initialize player variables and takes their symbols 
        playerOne = input("Choose your symbol (P1):")
        main()
        cont_game = input('Would you like to play again(Say No if no, otherwise input anything else)?')
        if cont_game == 'no' or cont_game =='No':
            break
        else:
            clear_grid()
    elif choice == "Computer":
        difficulty = input("What difficulty would you like to play in (easy/normal)?")
        playerOne = input("Choose your symbol:")
        main()
        cont_game = input('Would you like to play again(Say No if no, otherwise input anything else)?')
        if cont_game == 'no' or cont_game == 'No':
            break
        else:
            clear_grid()
        