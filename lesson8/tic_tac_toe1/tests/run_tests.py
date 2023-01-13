from lesson8.tic_tac_toe1.tests.board_tests import *

if __name__ == '__main__':
    # test column winner
    test_check_winner_column1()
    test_check_winner_column2()
    test_check_winner_column3()
    test_check_winner_column4()
    test_check_winner_column5()
    test_check_winner_column6()
    # test row winner
    test_check_winner_row1()
    test_check_winner_row2()
    test_check_winner_row3()
    test_check_winner_row4()
    test_check_winner_row5()
    test_check_winner_row6()
    # test diagonal winner
    test_check_winner_diagonal1()
    test_check_winner_diagonal2()
    test_check_winner_diagonal3()
    test_check_winner_diagonal4()
    test_check_winner_diagonal5()
    test_check_winner_diagonal6()
    # test row stuck
    test_is_game_stuck_row1()
    test_is_game_stuck_row2()
    # test column stuck
    test_is_game_stuck_column1()
    test_is_game_stuck_column2()
    test_is_game_stuck_column3()
    test_is_game_stuck_column4()
    # test diagonal stuck
    test_is_game_stuck_diagonal1()
    test_is_game_stuck_diagonal2()
    test_is_game_stuck_diagonal3()
    test_is_game_stuck_diagonal4()
