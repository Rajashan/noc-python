from p5 import *
from mover import Mover

def setup():
    size(640, 360)
    global mover
    global tx

    mover = Mover()
    mover.velocity = Vector(0, -0.3)

    tx = 0.01


def draw():
    global tx
    background(255)
    force = noise(tx) * 0.003
    tx += 0.01
    mover.apply_force_x(force)
    mover.update()
    mover.check_edges()
    mover.show()

run()