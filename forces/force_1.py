from p5 import *
from mover import Mover

def setup():
    size(640, 360)
    global mover_A
    global mover_B

    mover_A = Mover(width/4, 0, 1)
    mover_B = Mover(width/2, height/4, 5)


def draw():
    background(255)

    gravity = Vector(0.0, 0.1)

    gravity_A = gravity.copy()*mover_A.mass
    gravity_B = gravity.copy()*mover_B.mass



    mover_A.apply_force(gravity_A)
    mover_B.apply_force(gravity_B)

    if mouse_is_pressed:
        wind = Vector(0.1, 0)
        mover_A.apply_force(wind)
        mover_B.apply_force(wind)
    
    mover_A.check_edges()
    mover_A.update()
    mover_A.show()


    mover_B.check_edges()
    mover_B.update()
    mover_B.show()



run()