# checks if the board size is a digit and if it in the right range for the game
def check_board_size(size: str) -> bool:
    if size in ('3', '4', '5', '6', '7', '8', '9'):
        return True
    else:
        return False


# checks if the coordinates entered are numeric, are they in the range and checks rather the cell is empty or not.
def validate_coordinates(board: list[list], coordinates: list[str]) -> bool | tuple:
    if len(coordinates) == 2:
        if coordinates[0].strip() and coordinates[1].strip() in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
            numeric_coordinates: tuple = (int(coordinates[0].strip()), int(coordinates[1].strip()))
            if numeric_coordinates[0] and numeric_coordinates[1] in range(1, len(board) + 1):
                if board[numeric_coordinates[0] - 1][numeric_coordinates[1] - 1] is None:
                    return numeric_coordinates


# checks players names are not the same
def validate_names(name1: str, name2: str) -> bool:
    if name1 != name2:
        return True

