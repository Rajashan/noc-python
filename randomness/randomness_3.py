from p5 import *
from random import choice

def setup():
    size(640, 360)
    noLoop()

def draw():
    background(0)

    load_pixels()

    for x in range(width):
        for y in range(height):

            rand = choice(range(255))

            pixels[x, y] = (rand, rand, rand, 255)
    
    update_pixels()

run()