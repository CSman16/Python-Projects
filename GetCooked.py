#GetCooked.py 

#Game Description
print('''
Welcome to get cooked, where you have to cook something perfectly or else you will get
cooked to death by Gordon Ramsay. Here you have to manage a kitchen but the catch is 
you're blind. You can view the progress of different food items by typing "view (place)". 
There is the oven, stove, pan, saucepan, and a toaster. get 100 points to win or else 
Gordon will not be pleased...      
''')


#Importing
import time 
import random 
import pygame 


#Variables 
pan_view = False 
saucepan_view = False
oven_view = False 
toaster_view = False 
stove_view = False
seasoning_count = 5 
menu_items = ['sausage and waffles', 'bacon and eggs', 'chicken tenders and fries', 'cheeseburger and fries', 'mac & cheese',
'ice cream', 'seasoned steak']

#Game loop

while True:
    print('Welcome to the kitchen from hell.')
    time.sleep(0.5)
    print('YOU NEED TO COOK A', random.choice(menu_items))  # Use choice instead of random for selecting from a list
    terminal = input('Where would you like to go? ')
    
    if terminal == 'pan':
        # Add code to handle the 'pan' case here
        print("You are at the pan.")
    
    elif terminal == 'saucepan':  # Fixed the spelling from 'sausepan' to 'saucepan'
        # Add code to handle the 'saucepan' case here
        print("You are at the saucepan.")

    elif terminal == 'toaster': 
        # Add code to handle the 'toaster' case here
        print("You are at the toaster.")

    elif terminal == 'stove': 
        # Add code to handle the 'stove' case here
        print("You are at the stove.")

    elif terminal == 'oven': 
        # Add code to handle the 'oven' case here
        print("You are at the oven.")

    else: 
        print('Please enter a valid location. (Saucepan, Toaster, Oven, Stove, Pan)')