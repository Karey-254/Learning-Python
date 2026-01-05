# imports

# variables
world = '🌍🌎🌏'
python = 'Python 🐍'
fire = '🔥'

# Function definitions        
    
# Put code to run under here

print(f'Hello{world}')
print(f'Welcome to {python}')
print(f'{python} is good at Maths!')
print(f'{111111111 * 111111111}')

#imports
from datetime import datetime

# variables
print(f'The date and time is {datetime.now()}')

# Function definitions

def add_one_and_one():
    x = 1 + 1
    print(x)

def roll_dice():
    print(f'You rolled a {4}')

#Put code to run under here
print(f'The date and time is {datetime.now()}')
roll_dice()

# imports
from datetime import datetime
from random import randint

#Function definitions
def roll_dice():
    print(f'You rolled a {randint (1,6)}')

def roll_dice():
    roll = 'randint(1,6)'
    print(f'You rolled a {roll} {fire * roll}')
     #Input
def roll_dice():
    max = input('How many sides on your dice?:')
    print(f'That is a D {max}')
    roll = randint(1,6)
    print(f'You rolled a {roll} {fire * roll}')
    
