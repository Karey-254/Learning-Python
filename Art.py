from p5 import *
import random

WIDTH = 800
HEIGHT = 500

def setup():
    size(WIDTH, HEIGHT)
    background(15)
    no_loop()
    rect_mode(CENTER)

def draw():
    translate(WIDTH / 2, HEIGHT / 2)

    # Background texture
    for _ in range(300):
        stroke(40, 40, 40, 60)
        point(random.uniform(-WIDTH/2, WIDTH/2),
              random.uniform(-HEIGHT/2, HEIGHT/2))

    # Vehicle body (abstract chassis)
    no_stroke()
    fill(120, 180, 200, 200)
    rect(0, 0, 420, 90, 40)

    fill(90, 140, 160, 180)
    rect(40, -50, 220, 70, 30)

    # Wheels (motion-focused)
    wheel_positions = [(-150, 60), (150, 60)]
    for x, y in wheel_positions:
        draw_wheel(x, y)

    # Motion lines
    stroke(255, 120)
    for i in range(25):
        x = random.uniform(-300, 300)
        y = random.uniform(-100, 100)
        line(x, y, x - random.uniform(20, 80), y)

    # Energy accents
    no_fill()
    stroke(255, 100, 100, 120)
    for r in range(50, 200, 25):
        ellipse(0, 0, r * 2, r)

def draw_wheel(x, y):
    push_matrix()
    translate(x, y)

    # Outer wheel
    fill(30)
    no_stroke()
    ellipse(0, 0, 90, 90)

    # Inner motion spokes
    stroke(200)
    for angle in range(0, 360, 20):
        with push_matrix():
            rotate(radians(angle))
            line(0, 0, 45, 0)

    pop_matrix()

run()
