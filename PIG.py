# PIG

import random
import time

# keeps track of score
player_score = 0
player_points = 0
computer_score = 0
computer_points = 0

# Computer play variables
computer_roll = 0

# Flag to track if player's turn is over
player_turn_over = False

# Def function experiment
def turn_end():
    global player_turn_over
    player_turn_over = True

# Game loop
while True:  # Main game loop
    # Decides who goes first
    active_turn = random.randint(0, 1)

    # Player's turn code
    if active_turn == 1:
        player_turn_over = False
        while not player_turn_over:
            choice = input("Would you like to roll?:").lower()
            if choice == "yes":
                dice = random.randint(1, 6)
                if dice == 1:
                    print("You rolled a 1. ending turn.")
                    player_score -= player_points
                    player_points = 0
                    turn_end()
                else:
                    print("You rolled a", dice)
                    player_points += dice
                    player_score += dice
            elif choice == "no":
                if player_points > 0:
                    player_points = 0
                    turn_end()
                else:
                    turn_end()
            else:
                print("Please enter a valid response.")

    # Check for game end condition after player's turn
    if player_score >= 100:
        print("Game Over! You won!")
        break

    # Computer's turn code
    if active_turn == 0:
        computer_turn_over = False
        while not computer_turn_over:
            print("The computer is now playing")
            computer_roll = random.randint(0, 1)
            if computer_roll == 1:
                dice = random.randint(1, 6)
                if dice == 1:
                    print("The computer rolled a 1! ending turn...")
                    time.sleep(1)
                    computer_score -= computer_points
                    computer_points = 0
                    computer_turn_over = True
                else:
                    print("The computer rolled a", dice)
                    computer_points += dice
                    computer_score += dice
            else:
                print("The computer has ended their turn")
                time.sleep(1)
                computer_turn_over = True

    # Check for game end condition after computer's turn
    if computer_score >= 100:
        print("Game Over! Computer won!")
        break