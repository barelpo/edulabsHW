player1 = input("player1 insert you choice: ")
player2 = input("player2 insert your choice: ")
r = 'rock'
s = 'scissors'
p = 'paper'
player1_count = 0
player2_count = 0
game_amount = 0

while True:
    if (player1 == r and player2 == s) or (player1 == s and player2 == p) or (player1 == p and player2 == r):
        print('congratulations player 1')
        player1_count += 1
    elif player1 == player2:
        print('no winner')
    else:
        print('congratulations player 2')
        player2_count += 1
    game_amount += 1
    if input("would you like to play again? ") == "yes":
        player1 = input("player1 insert you choice: ")
        player2 = input("player2 insert your choice: ")

    else:
        break

print(f"end of game! \nwins for player 1: {player1_count} \nwins for player 2: {player2_count} \nevens: {game_amount - (player1_count + player2_count)}")
