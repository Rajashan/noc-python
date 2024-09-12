from p5 import *
from mover import Mover

def setup():
    size(640, 360)
    global mover
    mover = Mover()


def draw():
    background(255)
    mover.update_mouse()
    mover.check_edges()
    mover.show()

run()