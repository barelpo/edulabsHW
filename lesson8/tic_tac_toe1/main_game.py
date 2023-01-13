from lesson8.tic_tac_toe1.backend.board import *
from lesson8.tic_tac_toe1.frontend.board_print import *

print_greeting()

player1, player2 = get_names()

turn_counter = 0

player_char_dict = {
    player1: 'X',
    player2: 'O'
}

board = initialize_board()


while get_winner(board) is None and is_game_stuck(board) is None:
    print_board(board)
    if turn_counter % 2 == 0:
        turn = get_turn(board, player1)
        if turn:
            board = update_board(turn, player_char_dict[player1], board)
    if turn_counter % 2 == 1:
        turn = get_turn(board, player2)
        if turn:
            board = update_board(turn, player_char_dict[player2], board)
    turn_counter += 1


winner = get_winner(board)
game_stuck = is_game_stuck(board)
print_board(board)
if winner:
    print_win_message(winner, player_char_dict)
elif game_stuck:
    print("End of game, game is stuck!")


