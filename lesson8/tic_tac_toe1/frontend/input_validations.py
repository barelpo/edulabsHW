def check_board_size(size: str) -> bool:
    if size in ('3', '4', '5', '6', '7', '8', '9'):
        return True
    else:
        return False


def validate_coordinates(board: list[list], coordinates: list[str]) -> bool | tuple:
    if len(coordinates) == 2:
        if coordinates[0].strip() and coordinates[1].strip() in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
            numeric_coordinates: tuple = (int(coordinates[0].strip()), int(coordinates[1].strip()))
            if numeric_coordinates[0] and numeric_coordinates[1] in range(1, len(board) + 1):
                if board[numeric_coordinates[0] - 1][numeric_coordinates[1] - 1] is None:
                    return numeric_coordinates


def validate_names(name1: str, name2: str) -> bool:
    if name1 != name2:
        return True

