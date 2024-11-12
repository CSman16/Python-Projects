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
