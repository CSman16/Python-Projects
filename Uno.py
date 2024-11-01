#Uno in Python
import random
import time

game = 1
if game == 1:
    #intro
    print('''
        welcome to Uno! its like uno but in python and your arch nemesis this time is Python yet again. 
        the rules that are allowed in this game is stacking and that you can only draw one card before your turn is over. 
        you start with seven cards amd the first participant with no cards wins.
    ''')

num_players = 2


time.sleep(10)
def deck():
    uno_deck = []
    colors = ["blue","red","yellow","green"]
    numbers = [0,1,2,3,4,5,6,7,8,9]
    action_cards = ["Skip", "Draw 2", "Reverse", "Wild", "Wild Draw 4"]
    for color in colors:
        for number in numbers:
            card = (color, number)
            uno_deck.append(card)

deck()

def shuffle(uno_deck):
    random.shuffle(uno_deck)
    return uno_deck

shuffle(uno_deck)

def deal_cards(deck,num_cards):
    player_hand = random.sample(deck,num_cards)
    for card in player_hand:
        deck.remove(card)

        return uno_deck, player_hand
        
