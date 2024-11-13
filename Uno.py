#Uno in Python
import random
import time

game = 1
if game == 1:
    #intro
    print('''
        welcome to Uno! its like uno but in python and your arch nemesis this time is Python yet again. 
        the rules that are allowed in this game is stacking and that you can only draw one card before
        your turn is over. you start with seven cards and the first participant with no cards wins.
    ''')

num_players = 2
uno_deck = []

time.sleep(10)
def deck(uno_deck):
    uno_deck = []
    colors = ["blue","red","yellow","green"]
    numbers = [0,1,2,3,4,5,6,7,8,9]
    action_cards = ["Skip", "Draw 2", "Reverse"]
    for color in colors:
        for number in numbers:
            card = (color, number)
            uno_deck.append(card)
    for color in colors:
        for action in action_cards:
            card = (color, action)
            uno_deck.append(card)
            uno_deck.append(card)
    for _ in range(4):
        uno_deck.append(("Wild", "Wild"))
        uno_deck.append(("Wild", "Wild Draw 4"))
    return uno_deck
deck(uno_deck)
uno_deck = deck(uno_deck)
def shuffle(uno_deck):
    random.shuffle(uno_deck)
    return uno_deck

shuffle(uno_deck)

num_cards = 7

def deal_cards(uno_deck,num_cards):
    player_hand = random.sample(uno_deck,num_cards)
    for card in player_hand:
        uno_deck.remove(card)

    python_hand = random.sample(uno_deck, num_cards)

    for card in python_hand:
        uno_deck.remove(card)
    return uno_deck, player_hand, python_hand

uno_deck, player_hand, python_hand = deal_cards(uno_deck, num_cards)
print("your hand:", player_hand)

def start_game(uno_deck):
    while True:
        first_card = uno_deck.pop(0)
        if first_card[0] != "Wild":
            break
        else:
            uno_deck.append(first_card)
            random.shuffle(uno_deck)

    print("Starting Card: ", first_card)
    starting_color, starting_value = first_card
    
    return uno_deck, starting_color, starting_value

uno_deck, current_color, current_value = start_game(uno_deck)

def game_loop(uno_deck, player_hand, python_hand, current_color, current_value):
    player_turn = True
    while True:
        print(f"\nCurrent Card: {current_color} {current_value}")

        if player_turn:
            print("\nYour Hand:", player_hand)
            playable_cards = [card for card in player_hand if card[0] == current_color or card[1] ==current_value or card[0] == "Wild"]

            if playable_cards:
                print("playable cards:", playable_cards)
                while True:
                    for index, card in enumerate(player_hand):
                        print(f"{index}: {card}")

                    try:
                        choice = int(input("choose a card to play by index (or type -1 to draw): "))

                        if choice == -1:
                            new_card = uno_deck.pop(0)
                            player_hand.append(new_card)
                            print("you drew:", new_card)
                            break

                        chosen_card = player_hand[choice]
                        if chosen_card in playable_cards:
                            player_hand.remove_chosen_card
                            print("you played:", chosen_card)
                            current_color, current_value = chosen_card
                            break
                        else:
                            print("Invalid choice! Please pick a matching card")
                    except(ValueError, IndexError):
                        print("Invalid Input! Please enter a valid card index or -1 to draw.")
                        
                        
    else:
        playable_cards = [card for card in python_hand if card[0] == current_color or card[1] == current_value or card[0] == "Wild"]

        if playable_cards:
            chosen_card = playable_cards[0]
            python_hand.remove(chosen_card)
            print("\nPython placed:", chosen_card)
            print("\nPython has", len(python_hand), "cards left")
            current_color, current_value = chosen_card
        else:
            new_card = uno_deck.pop[0]
            python_hand.appen(new_card)
            random.shuffle(python_hand)
            print("\nPython had no playable cards and drew a card")

            player_turn = True

    if len(player_hand) == 0:
        print("You are the winner!")
        break
        
    elif len(python_hand) == 0:
        break
