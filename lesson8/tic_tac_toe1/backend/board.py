from lesson8.tic_tac_toe1.frontend.utils import *


# initialize board according to the size the user chose
def initialize_board() -> list[list]:
    size: int = board_size()
    board: list = []
    for i in range(0, size):
        board.append([])
        for j in range(0, size):
            board[i].append(None)
    return board


# updates board with users char according to the place he chose on the board
def update_board(coordinates: tuple, char: str, board: list[list]) -> list[list]:
    board[int(coordinates[0]) - 1][int(coordinates[1]) - 1] = char
    return board


# checks if there is a winner according to board current state using the three functions below
def get_winner(board: list[list]) -> str | None:
    column_winner = check_winner_column(board)
    row_winner = check_winner_row(board)
    diagonal_winner = check_winner_diagonal(board)
    if row_winner:
        return row_winner
    elif column_winner:
        return column_winner
    elif diagonal_winner:
        return diagonal_winner


# checks if there is a winner by row according to board current state
def check_winner_row(board: list[list]) -> str | None:
    count: int = 0
    for i, val_row in enumerate(board):
        count: int = 0
        for j in range(1, len(board[i])):
            if board[i][j] == board[i][j-1]:
                count += 1
        if count == len(board) - 1:
            if board[i][0] == 'O':
                return 'O'
            elif board[i][0] == 'X':
                return 'X'


# checks if there is a winner by column according to board current state
def check_winner_column(board: list[list]) -> str | None:
    counters: list = []
    for i in range(0, len(board)):
        counters.append(1)
    for i in range(1, len(board)):
        for j, val_column in enumerate(board[i]):
            if val_column == board[i-1][j] and val_column is not None:
                counters[j] += 1
    for i, counter in enumerate(counters):
        if counter == len(board):
            return board[0][i]


# checks if there is a winner by diagonal according to board current state
def check_winner_diagonal(board: list[list]) -> str | None:
    counter_main = 0
    counter_secondary = 0
    for i in range(1, len(board)):
        for j, val_column in enumerate(board[i]):
            if j == i and board[i - 1][j - 1] == val_column:
                counter_main += 1
            if j == len(board) - 1 - i and val_column == board[i - 1][j + 1]:
                counter_secondary += 1
    if counter_main == len(board) - 1:
        return board[0][0]
    elif counter_secondary == len(board) - 1:
        return board[-1][0]


# checks if the game is stuck according to current board state, using the three functions below
def is_game_stuck(board: list[list]) -> bool | None:
    if is_game_stuck_row(board):
        return True
    elif is_game_stuck_column(board):
        return True
    elif is_game_stuck_diagonal(board):
        return True
    else:
        return


# checks if the game is stuck by all rows, according to current board state
def is_game_stuck_row(board: list[list]) -> bool | None:
    counter_stuck_rows: int = 0
    for i, val_row in enumerate(board):
        counter_x: int = 0
        counter_o: int = 0
        for j, val_cell in enumerate(board[i]):
            if val_cell == 'O':
                counter_o += 1
            elif val_cell == 'X':
                counter_x += 1
        if counter_x > 0 and counter_o > 0:
            counter_stuck_rows += 1
    if counter_stuck_rows == len(board):
        return True
    else:
        return


# checks if the game is stuck by all columns, according to current board state
def is_game_stuck_column(board: list[list]) -> bool | None:
    counters_o: list[int] = []
    counters_x: list[int] = []
    for i in range(0, len(board)):
        counters_o.append(0)
        counters_x.append(0)
    for i in range(0, len(board)):
        for j, val_cell in enumerate(board[i]):
            if val_cell == 'O':
                counters_o[j] += 1
            elif val_cell == 'X':
                counters_x[j] += 1
    if 0 in counters_x or 0 in counters_o:
        return
    else:
        return True


# checks if the game is stuck by both diagonals, according to current board state
def is_game_stuck_diagonal(board: list[list]) -> bool | None:
    counters_x: list[int] = [0, 0]
    counters_o: list[int] = [0, 0]
    for i in range(0, len(board)):
        for j, val_cell in enumerate(board[i]):
            if i == j:
                if val_cell == 'X':
                    counters_x[0] += 1
                elif val_cell == 'O':
                    counters_o[0] += 1
            if j == len(board) - 1 - i:
                if val_cell == 'X':
                    counters_x[1] += 1
                elif val_cell == 'O':
                    counters_o[1] += 1
    if 0 in counters_x or 0 in counters_o:
        return
    else:
        return True














