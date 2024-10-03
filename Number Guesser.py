import random
import time

secret_number = random.randint(0,1000000)
tries = 0

print("Welcome to the number guessing game where you guess a number between 0 and 1000000!")
print ("You have 20 guesses and hints will be provided via greater than or lower than!")
time.sleep(2)

while tries != 21:
    print("you have guessed", tries, "time(s).")
    user_guess = int(input("What is your guess?"))
    if user_guess == secret_number:
        print("Congrats! you guessed correctly. Heres a cookie.")
        break
    elif user_guess > secret_number: 
        print("the secret number is lower than your number")
        print()
        tries = tries + 1
    elif user_guess < secret_number:
        print("the secret number is higher than your number")
        print()
        tries = tries + 1
    else:
        print("Please enter a valid integer")
else:
    print("You failed to guess the number within 20 tries. The number was", secret_number, "I will be taking your cookies now!")
    time.sleep(2)

