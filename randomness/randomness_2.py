from p5 import *
from random import gauss

def setup():
    size(640, 240)

def draw():
    x = gauss(320, 60)

    noStroke()

    fill(0, 10)

    circle(x, 120, 16)

run()