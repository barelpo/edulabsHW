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
        'X shoul be the winner'


def test_check_winner_column3():
    board = [
        [None, 'O', None],
        [None, 'O', None],
        [None, 'O', None]
    ]
    ret_val = check_winner_column(board)
    assert ret_val == 'O', \
        'O shoul be the winner'


def test_check_winner_column4():
    board = [
        [None, 'O', 'X', None],
        ['O', 'O', 'X', 'X'],
        [None, 'X', 'X', 'O'],
        ['X', 'O', 'X', None]
    ]
    ret_val = check_winner_column(board)
    assert ret_val == 'X', \
        'X shoul be the winner'


def test_check_winner_column5():
    board = [
        [None, 'O', 'X'],
        ['O', 'O', None],
        [None, 'X', None]
    ]
    ret_val = check_winner_column(board)
    assert ret_val is None, \
        'no winner shoul be detected'


# check row winner
def test_check_winner_row1():
    board = [
        [None, 'O', 'X'],
        ['O', 'O', None],
        [None, 'X', None]
    ]
    ret_val = check_winner_row(board)
    assert ret_val is None, \
        'no winner shoul be detected'


def test_check_winner_row2():
    board = [
        [None, 'O', 'X', None],
        ['O', 'O', 'O', 'O'],
        [None, 'X', None, 'X'],
        ['O', 'X', None, 'O']
    ]
    ret_val = check_winner_row(board)
    assert ret_val == 'O', \
        'O shoul be the winner'


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
        'Xshould be the winner'


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


# check diagonal winner
def test_check_winner_diagonal1():
    board = [
        [None, 'O', 'X'],
        ['O', 'O', None],
        [None, 'X', None]
    ]
    ret_val = check_winner_diagonal(board)
    assert ret_val is None, \
        'no winner shoul be detected'


def test_check_winner_diagonal2():
    board = [
        ['O', 'O', 'X', None],
        ['O', 'O', 'O', 'X'],
        [None, 'X', 'O', 'X'],
        ['O', 'X', None, 'O']
    ]
    ret_val = check_winner_diagonal(board)
    assert ret_val == 'O', \
        'O shoul be the winner'


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
    assert ret_val == 'O', \
        'no winner should be detected'
