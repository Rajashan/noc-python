from p5 import *
from mover import Mover

def setup():
    size(640, 360)
    global mover
    mover = Mover()


def draw():

    background(255)

    if key == "UP":
        mover.acceleration.x += 0.05
        mover.acceleration.y += 0.05
    elif key == "DOWN":
        mover.acceleration.x -= 0.05
        mover.acceleration.y -= 0.05

    mover.update()
    mover.check_edges()
    mover.show()
    

run()