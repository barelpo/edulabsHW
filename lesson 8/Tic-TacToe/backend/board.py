def initialize_board(size: int) -> list[list]:
    board: list = []
    for i in range(0, size):
        board.append([])
        for j in range(0, size):
            board[i].append(None)
    return board


def update_board(coordinates: tuple[str, str], char: str, board: list[list]) -> list[list]:
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
    for i in range(0, len(board) - 1):
        counters.append(1)
    for i in range(1, len(board) - 1):
        for j, val_column in enumerate(board[i]):
            if val_column == board[i-1][j]:
                counters[j] += 1
    for i, counter in counters:
        if i == 3:
            return board[0][i]


def check_winner_diagonal(board: list[list]) -> str | None:

