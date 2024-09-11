from p5 import *

from numpy import interp
from math import floor

def setup():
    size(640, 360)
    global z_off
    z_off = 0.0



def draw():
    background(0)
    global z_off
    load_pixels()

    x_off = 0.0
    z_off += 0.01
    for x in range(width):
        y_off = 0.0
        x_off += 0.01

        for y in range(height):


            y_off += 0.01
            bright = floor(interp(noise(x_off, y_off, z_off), [0, 1], [0, 255])) + 1

            pixels[x, y] = (bright, bright, bright, 255)

    update_pixels()

    z_off += 0.01

run()