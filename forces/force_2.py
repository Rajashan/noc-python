from p5 import *
from mover import Mover

def setup():
    size(640, 360)
    global mover

    mover = Mover(width/4, 0, 1)

def draw():
    background(255)

    gravity = Vector(0.0, 0.1)

    gravity = gravity*mover.mass



    mover.apply_force(gravity)

    if mouse_is_pressed:
        wind = Vector(0.1, 0)
        mover.apply_force(wind)
    """"
    if mouse_is_pressed:
        TODO: implement mouse throwing
    """
    if mover.contact_edge():
        c = 0.1
        friction = mover.velocity.copy()
        friction *= -1
        friction = friction.normalize() * c

        mover.apply_force(friction)

    mover.bounce_edges()
    mover.check_edges()
    mover.update()
    mover.show()


run()