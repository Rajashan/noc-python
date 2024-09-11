from walker import Walker, PerlinWalker
from p5 import *

def setup():
    size(640, 360)
    global w
    w = PerlinWalker()
    background(255)


def draw():
    w.size_step()
    w.show()

run()