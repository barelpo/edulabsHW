def initialize_board(size: int) -> list[list]:
    board: list = []
    for i in range(0, size):
        board.append([])
        for j in range(0, size):
            board[i].append(None)
    return board


def update_board(coordinates: tuple, char: str, board: list[list]) -> list[list]:
    board[int(coordinates[0]) - 1][int(coordinates[1]) - 1] = char
    return board


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


def check_winner_diagonal(board: list[list]) -> str | None:
    counter_main = 0
    counter_secondary = 0
    for i in range(1, len(board)):
        for j, val_column in enumerate(board[i]):
            if j == i and board[i - 1][j - 1] == val_column:
                counter_main += 1
            if j == len(board) - 1 - i and board[i - 1][j + 1]:
                counter_secondary += 1
    if counter_main == len(board) - 1:
        return board[0][0]
    elif counter_secondary == len(board) - 1:
        return board[-1][0]






















