# prints current state of the board before each turn and at the end of game
def print_board(board: list[list]):
    for i in range(0, 6 * len(board) + 4):
        if i % 6 == 0 and i > 0:
            print(int(i / 6), end='')
        else:
            print(' ', end='')

    print('\n')
    row_counter: int = 1

    for i in range(0, 2 * len(board)):
        if i % 2 == 0:
            print('   ' + (6 * len(board) * '-'))
        else:
            print(f"{row_counter}  |", end='')
            for j in board[row_counter - 1]:
                if j:
                    print(f"  {j}  |", end='')
                else:
                    print(f"     |", end='')
            print('\n')
            row_counter += 1



