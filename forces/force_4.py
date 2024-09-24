from p5 import *
from mover import Mover
from attractor import Attractor 

def setup():
    size(640, 360)
    global mover
    global attractor
    global G 

    mover = Mover(300, 50, 2)
    attractor = Attractor()
    G = 1.0

def draw():
    background(255)

    force = attractor.attract(mover)
    mover.apply_force(force)
    mover.update()
    attractor.show()
    mover.show()
run()