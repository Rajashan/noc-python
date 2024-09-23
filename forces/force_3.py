from p5 import *
from mover import Mover
from liquid import Liquid
from random import random


def setup():
    size(640, 240)
    global liquid
    global movers
    movers = []

    for i in range(9):
        mass = random() * 5

        movers.append(Mover(40 + i * 70, 0, mass))
    

    liquid = Liquid(0, height / 2, width, height / 2, 0.1)

def draw():
    background(255)

    liquid.show()

    for i in range(len(movers)):

        if liquid.contains(movers[i]):
            drag_force = liquid.calculate_drag(movers[i])
            movers[i].apply_force(drag_force)

        gravity = Vector(0, 0.1 * movers[i].mass)

        movers[i].apply_force(gravity)

        movers[i].update()
        movers[i].show()
        movers[i].check_edges()

run()