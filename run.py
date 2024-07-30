import os
import random

game_grid = []
player_choice_history = []
computer_choice_history = []


def check_target_status(target):
    """
    Checking the target if it is diagonal or vertical or horiz
    """
    for i in range(3):
        # If the cell is to the absolute left
        if i % 3 == 0:
            # Check if 3 consecutive cells are selected (e.g., 123, 456, 789)
            if i in target and i + 1 in target and i + 2 in target:
                return True
        # If the value is below 3, check if any vertically consecutive cells
        # are selected from top to bottom (e.g., 147, 258, 369)
        if i < 3:
            if i in target and i + 3 in target and i + 6 in target:
                return True

    # Checking diagonal top left to bottom right
    if 0 in target and 4 in target and 8 in target:
        return True
    # Checking diagonal top right to bottom left
    if 2 in target and 4 in target and 6 in target:
        return True
    # If none of the above returned true
    return False


def computer_choose():
    """
    Computer chooses a position for its move
    """
    choice = -1
    while True:
        # Choosing a random number from the valid cells in the grid
        random_choice = random.randint(0, 8)
        # Checking if the random choice collides with a previous choice
        if random_choice not in player_choice_history:
            if random_choice not in computer_choice_history:
                # If it doesn't, choose this cell and break out of the loop.
                # Else, repeat until it doesn't collide
                choice = random_choice
                break
    return choice


def gen_game_grid():
    """
    Player and computer choice
    """
    to_return = ""
    for j in range(9):
        if j in player_choice_history:
            i = "X"
        elif j in computer_choice_history:
            i = "O"
        else:
            i = j + 1

        if (j + 1) % 3 == 0:
            to_return += f"{i}\n"
        else:
            to_return += f"{i} | "

    return to_return

is_gameover = False
print("Welcome to X||O (The Game)).")
print("You play as X, Computer plays as O")
while True:
    print(gen_game_grid())
    if(is_gameover):
        _user_input = input("r to start a new game, or q to quit")
        if(_user_input == "q"):
            break
        elif(_user_input == "r"):
            game_grid = []
            player_choice_history = []
            computer_choice_history = [] 
            is_gameover = False
            print(gen_game_grid())

    user_input = input("Choose a number from the grid; or q to quit game: \n")
    if user_input == "q":
        print("Thanks for playing the game.")
        break
    if user_input.isdigit():
        user_input = int(user_input)
    else:
        print("Invalid entry")
        continue

    player_choice_history.append(user_input - 1)
    if check_target_status(player_choice_history):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You won. Good job.")
        is_gameover = True
    elif len(computer_choice_history) + len(player_choice_history) >= 9:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("It's a tie, better luck next time.")
        is_gameover = True
    else:
        computer_choice_history.append(computer_choose())
        if check_target_status(computer_choice_history):
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Computer won. Better luck next time.")
            is_gameover = True
    
    if not is_gameover:
        os.system('cls' if os.name == 'nt' else 'clear')
