from lesson8.tic_tac_toe1.backend.board import *


# check column winner
def test_check_winner_column1():
    board = [
        [None, None, None],
        [None, None, None],
        [None, None, None]
    ]
    ret_val = check_winner_column(board)
    assert ret_val is None, \
        'Detected a winner in an empty board'


def test_check_winner_column2():
    board = [
        ['X', None, None],
        ['X', None, None],
        ['X', None, None]
    ]
    ret_val = check_winner_column(board)
    assert ret_val == 'X', \
        'X should be the winner'


def test_check_winner_column3():
    board = [
        [None, 'O', None],
        [None, 'O', None],
        [None, 'O', None]
    ]
    ret_val = check_winner_column(board)
    assert ret_val == 'O', \
        'O should be the winner'


def test_check_winner_column4():
    board = [
        [None, 'O', 'X', None],
        ['O', 'O', 'X', 'X'],
        [None, 'X', 'X', 'O'],
        ['X', 'O', 'X', None]
    ]
    ret_val = check_winner_column(board)
    assert ret_val == 'X', \
        'X should be the winner'


def test_check_winner_column5():
    board = [
        [None, 'O', 'X'],
        ['O', 'O', None],
        [None, 'X', None]
    ]
    ret_val = check_winner_column(board)
    assert ret_val is None, \
        'no winner should be detected'


def test_check_winner_column6():
    board = [
        ['X', 'O', 'O'],
        ['X', 'X', 'O'],
        ['O', 'X', None]
    ]
    ret_val = check_winner_column(board)
    assert ret_val is None, \
        'no winner should be detected'


# check row winner
def test_check_winner_row1():
    board = [
        [None, 'O', 'X'],
        ['O', 'O', None],
        [None, 'X', None]
    ]
    ret_val = check_winner_row(board)
    assert ret_val is None, \
        'no winner should be detected'


def test_check_winner_row2():
    board = [
        [None, 'O', 'X', None],
        ['O', 'O', 'O', 'O'],
        [None, 'X', None, 'X'],
        ['O', 'X', None, 'O']
    ]
    ret_val = check_winner_row(board)
    assert ret_val == 'O', \
        'O should be the winner'


def test_check_winner_row3():
    board = [
        [None, 'O', 'X', None, 'X'],
        ['O', 'O', 'O', 'O', 'X'],
        ['X', 'X', 'X', 'X', 'X'],
        ['O', 'X', None, 'O', 'O'],
        ['O', 'X', 'X', None, 'O']
    ]
    ret_val = check_winner_row(board)
    assert ret_val == 'X', \
        'X should be the winner'


def test_check_winner_row4():
    board = [
        [None, None, None, None, None],
        [None, None, None, None, None],
        [None, None, None, None, None],
        [None, None, None, None, None],
        [None, None, None, None, None]
    ]
    ret_val = check_winner_row(board)
    assert ret_val is None, \
        'no winner should be detected'


def test_check_winner_row5():
    board = [
        [None, None, None, None, None],
        [None, None, None, None, None],
        [None, None, None, None, None],
        [None, None, None, None, None],
        ['O', 'O', 'O', 'O', 'O']
    ]
    ret_val = check_winner_row(board)
    assert ret_val == 'O', \
        'no winner should be detected'


def test_check_winner_row6():
    board = [
        ['X', 'O', 'O'],
        ['X', 'X', 'O'],
        ['O', 'X', None]
    ]
    ret_val = check_winner_row(board)
    assert ret_val is None, \
        'no winner should be detected'


# check diagonal winner
def test_check_winner_diagonal1():
    board = [
        [None, 'O', 'X'],
        ['O', 'O', None],
        [None, 'X', None]
    ]
    ret_val = check_winner_diagonal(board)
    assert ret_val is None, \
        'no winner should be detected'


def test_check_winner_diagonal2():
    board = [
        ['O', 'O', 'X', None],
        ['O', 'O', 'O', 'X'],
        [None, 'X', 'O', 'X'],
        ['O', 'X', None, 'O']
    ]
    ret_val = check_winner_diagonal(board)
    assert ret_val == 'O', \
        'O should be the winner'


def test_check_winner_diagonal3():
    board = [
        [None, 'O', 'X', None, 'X'],
        ['O', 'O', 'O', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X'],
        ['O', 'X', None, 'O', 'O'],
        ['X', 'X', 'X', None, 'O']
    ]
    ret_val = check_winner_row(board)
    assert ret_val == 'X', \
        'X should be the winner'


def test_check_winner_diagonal4():
    board = [
        [None, None, None, None, None],
        [None, None, None, None, None],
        [None, None, None, None, None],
        [None, None, None, None, None],
        [None, None, None, None, None]
    ]
    ret_val = check_winner_row(board)
    assert ret_val is None, \
        'no winner should be detected'


def test_check_winner_diagonal5():
    board = [
        ['O', None, None, None, 'X'],
        [None, 'O', None, 'X', None],
        [None, None, 'X', None, None],
        [None, 'X', None, None, None],
        ['O', 'X', 'O', 'O', 'O']
    ]
    ret_val = check_winner_diagonal(board)
    assert ret_val is None, \
        'no winner should be detected'


def test_check_winner_diagonal6():
    board = [
        ['X', 'O', 'O'],
        ['X', 'X', 'O'],
        ['O', 'X', None]
    ]
    ret_val = check_winner_diagonal(board)
    assert ret_val is None, \
        'no winner should be detected'


def test_is_game_stuck_row1():
    board5 = [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None]
    ]
    ret_val = is_game_stuck_row(board5)
    assert ret_val is None, 'game is not stuck'


def test_is_game_stuck_row2():
    board2 = [
        ['X', 'O', None, None, None],
        [None, None, 'O', None, 'X'],
        ['X', 'X', 'X', 'X', 'O'],
        ['O', None, 'X', 'O', None],
        [None, 'O', None, 'X', None]
    ]
    ret_val = is_game_stuck_row(board2)
    assert ret_val is True, 'game is stuck'


def test_is_game_stuck_row3():
    board2 = [
        ['X', 'O', 'X', 'O', 'X'],
        ['O', 'X', 'O', 'X', 'O'],
        [None, None, None, None, None],
        [None, None, None, None, None],
        [None, None, None, None, None]
    ]
    ret_val = is_game_stuck_diagonal(board2)
    assert ret_val is None, 'game is not stuck'


def test_is_game_stuck_column1():
    board2 = [
        ['X', 'O', 'O', None, None],
        [None, None, 'O', None, 'X'],
        ['X', 'X', 'X', 'X', 'O'],
        ['O', None, 'X', 'O', None],
        [None, 'O', None, 'X', None]
    ]
    ret_val = is_game_stuck_column(board2)
    assert ret_val is True, 'game is stuck'


def test_is_game_stuck_column2():
    board2 = [
        ['X', 'O', 'O', None, None],
        [None, None, 'O', None, 'X'],
        ['X', 'X', 'X', 'X', 'O'],
        ['O', None, 'X', 'X', None],
        [None, 'O', None, 'X', None]
    ]
    ret_val = is_game_stuck_column(board2)
    assert ret_val is None, 'game is not stuck'


def test_is_game_stuck_column3():
    board5 = [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None]
    ]
    ret_val = is_game_stuck_column(board5)
    assert ret_val is None, 'game is not stuck'


def test_is_game_stuck_column4():
    board5 = [
        ['X', None, None, None, 'O', None, None, None],
        [None, None, 'X', 'O', None, None, 'O', None],
        [None, None, None, None, None, 'X', None, 'O'],
        [None, 'O', None, 'X', None, 'O', None, None],
        [None, None, 'O', None, 'X', None, None, 'O'],
        [None, None, None, None, None, None, None, 'X'],
        [None, 'X', None, None, 'O', None, 'O', None],
        ['O', None, None, None, None, None, 'X', None]
    ]
    ret_val = is_game_stuck_column(board5)
    assert ret_val is True, 'game is stuck'


def test_is_game_stuck_column5():
    board2 = [
        ['X', 'O', 'X', 'O', 'X'],
        ['O', 'X', 'O', 'X', 'O'],
        [None, None, None, None, None],
        [None, None, None, None, None],
        [None, None, None, None, None]
    ]
    ret_val = is_game_stuck_diagonal(board2)
    assert ret_val is True, 'game is stuck'


def test_is_game_stuck_diagonal1():
    board2 = [
        ['X', 'O', 'O', None, None],
        [None, None, 'O', None, 'X'],
        ['X', 'X', 'X', 'X', 'O'],
        ['O', None, 'X', 'O', None],
        ['O', 'O', None, 'X', None]
    ]
    ret_val = is_game_stuck_diagonal(board2)
    assert ret_val is True, 'game is stuck'


def test_is_game_stuck_diagonal2():
    board2 = [
        ['X', 'O', 'O', None, None],
        [None, None, 'O', 'O', 'X'],
        ['X', 'X', 'X', 'X', 'O'],
        ['O', None, 'X', 'X', None],
        [None, 'O', None, 'X', None]
    ]
    ret_val = is_game_stuck_diagonal(board2)
    assert ret_val is None, 'game is not stuck'


def test_is_game_stuck_diagonal3():
    board5 = [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None]
    ]
    ret_val = is_game_stuck_diagonal(board5)
    assert ret_val is None, 'game is not stuck'


def test_is_game_stuck_diagonal4():
    board5 = [
        ['X', None, None, None, 'O', None, None, None],
        [None, None, 'X', 'O', None, None, 'O', None],
        [None, None, None, None, None, 'X', None, 'O'],
        [None, 'O', None, 'X', None, 'O', None, None],
        [None, None, 'O', None, 'X', None, None, 'O'],
        [None, None, None, None, None, None, None, 'X'],
        [None, 'X', None, None, 'O', None, 'O', None],
        ['O', None, None, None, None, None, 'X', None]
    ]
    ret_val = is_game_stuck_diagonal(board5)
    assert ret_val is True, 'game is stuck'


def test_is_game_stuck_diagonal5():
    board2 = [
        ['X', 'O', 'X', 'O', 'X'],
        ['O', 'X', 'O', 'X', 'O'],
        [None, None, None, None, None],
        [None, None, None, None, None],
        [None, None, None, None, None]
    ]
    ret_val = is_game_stuck_diagonal(board2)
    assert ret_val is None, 'game is not stuck'