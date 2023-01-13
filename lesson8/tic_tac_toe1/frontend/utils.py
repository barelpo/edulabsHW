from lesson8.tic_tac_toe1.frontend.input_validations import *


# print welcome greeting
def print_greeting():
    print('Welcome to the Tic Tac Toe game !!')


# gets players ames
def get_names() -> tuple:
    while True:
        player1: str = input("Please insert the name of player 1: ")
        player2: str = input("Please insert the name of player 2: ")
        if validate_names(player1, player2):
            break
        else:
            print("Names can't be exactly the same!")
    names = (player1, player2)
    return names


# gets board size from user
def board_size() -> int:
    while True:
        size = input("Insert the board size for your game (min: 3x3, max: 9x9): ")
        if check_board_size(size):
            return int(size)
        else:
            print("Incorrect input. Input is not a number or not in the given range.")


# gets from user the cell coordinates he chose on the board for each turn
def get_turn(board: list[list], player: str) -> tuple:
    while True:
        turn = input(f"{player} Insert cell coordinates separated by ',' (firs line and than column): ").strip()
        coordinates = turn.split(',')
        numeric_coordinates = validate_coordinates(board, coordinates)
        if numeric_coordinates:
            return numeric_coordinates
        else:
            print("Invalid move, choose again.")


# prints message when winner detected
def print_win_message(char: str, names_to_char: dict):
    for key in names_to_char:
        if names_to_char[key] == char:
            print(f"Congratulations, {key} is the winner !!")

