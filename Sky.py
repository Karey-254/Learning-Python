# Import library code
from p5 import *
from random import randint

# The mouse_pressed function goes here



# The shoot_arrow function goes here



def setup():
    # Setup your game here
    size(400, 400)
    no_stoke()


def draw():
    # Things to do in every frame
    fill('cyan')
    rect(0, 0, 400, 250)
    fill('lightgreen')
    rect(0, 250, 400, 150)
    fill('sienna')
    triangle(150, 350, 200, 150, 250, 350)

# Keep this to run your code
run(frame_rate=2)