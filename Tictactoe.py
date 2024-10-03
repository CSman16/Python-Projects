# Tic Tac Toe

import random


Turn = 0
spots =["top left","top center","top right","center left","center","center right","bottom left","bottom center", "bottom right"]
print("To place a piece, you must type it exactly as shown below!")
print(spots)
computer_placement = random.choice[spots]

while turn == 1:
    print("It is your turn")
    user_placement = input("Where will you place your piece?:")
