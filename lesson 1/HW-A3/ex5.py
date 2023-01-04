player1 = input("player1 insert you choice: ")
player2 = input("player2 insert your choice: ")
r = 'rock'
s = 'scissors'
p = 'paper'

if (player1 == r and player2 == s) or (player1 == s and player2 == p) or (player1 == p and player2 == r):
    print('congratulations player 1')
elif player1 == player2:
    print('no winner')
else:
    print('congratulations player 2')
