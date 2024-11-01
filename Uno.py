#Uno in Python
import random

def deck():
    uno_deck = []
    colors = ["blue","red","yellow","green"]
    numbers = [0,1,2,3,4,5,6,7,8,9]
    for color in colors:
        uno_deck.append(colors)
        uno_deck.append(numbers)
        print(uno_deck)
       
deck()




#intro
print('''
    Welcome to Uno! it's like uno but in Python and your arch nemesis, this time is Python again. 
    The rules allowed in this game are stacking, and you can only draw one card before your turn is over. 
    you start with seven cards and the first participant with no cards wins.
''')
