from p5 import *

def setup():
    size(640, 240)
    global position
    global velocity

    position = Vector(100, 100)
    velocity = Vector(2.5, 2)

def draw():
    global position
    global velocity
    background(255)
    position += velocity

    if (position.x > width or position.x < 0):
        velocity.x = -velocity.x
    if (position.y > height or position.y < 0):
        velocity.y = -velocity.y
    
    stroke(0)
    fill(127)
    circle(position.x, position.y, 48)

run()