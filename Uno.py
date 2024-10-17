#Uno
# imports
import random
import time

# cards storage
colors = ['red', 'blue', 'yellow', 'green']
numbers = list(range(0, 10))
action_cards = ['skip', 'reverse', 'plus 2']
wild_cards = ['wild card', 'wild draw four']

#deck creation
def create_deck():
    #Deck placeholder
    deck = []
    #  Adding number cards (1 zero card per color, 2 of each 1-9 card per color)
    for color in colors:
        deck.append((color, '0'))
        #two of each 1-9 card
        for number in numbers[1:]: #excluding zero
            deck.append((color, str(number)))
            deck.append((color, str(number)))

# Adding action cards (2 of each per color)
    for clor in colors:
        for action in action_cards:
            deck.append((color, action))
            deck.append((color, action))

    for wild in wild_cards:
        for _ in range(4):
            deck.append(('wind', wild))


    return deck

#Shuffling Deck
def shuffle_deck(deck):
    random.shuffle(deck)
    return deck

#hands
def deal_hands(deck, num_players,cards_per_player):
    hands = {f'Player {i+1}': [] for i in range(num_players)} # creates a dictionary for hands
    for _ in range(cards_per_player):
        for player in hands.keys():
            if deck:
                hands[player].append(deck.pop(0))
    return hands


#create and shuffle the deck
uno_deck = create_deck()
uno_deck = shuffle_deck(uno_deck)

#define num of players and hand size
num_players = 2
cards_per_player = 7

#intro
print('''
    welcome to Uno! its like uno but in python and your arch nemesis this time is Python yet again. 
    the rules that are allowed in this game is stacking and that you can only draw one card before your turn is over. 
    you start with seven cards amd the first participant with no cards wins.
''')

#deal hands
player_hands = deal_hands(uno_deck, num_players, cards_per_player)

for player in player_hands:
    print(f"{player}'s hand: {hand}")
