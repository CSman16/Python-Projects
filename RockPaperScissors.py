import random

user_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type rock/paper/scissors or q to stop: ").lower()
    
    if user_input == "q":
        break

    elif user_input not in options:
        continue
    
    computer_choice = random.choice(options)
    print("Computer picked", computer_choice + ".")

    if user_input == "rock" and computer_choice == "scissors":
        print("You won!")
        user_wins += 1

    elif user_input == "paper" and computer_choice == "rock":
        print("You won!")
        user_wins += 1
    elif user_input == "scissors" and computer_choice == "paper":
        print("You won!")
        user_wins += 1
    elif user_input == computer_choice:
        print("It was a tie!")
        continue
    else:
        print("You lost!")
        computer_wins += 1

print("Final score - You:", user_wins, "Computer:", computer_wins)
