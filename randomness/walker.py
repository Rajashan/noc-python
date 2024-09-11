from math import floor
from numpy import interp
from random import random, uniform, randint, gauss

from p5 import *

class Walker(object):
    
    def __init__(self):
        self.x = width / 2
        self.y = height / 2

    def show(self):
        stroke(0)
        point(self.x, self.y)


    def step(self):
        choice = floor(randint(0,3))

        if choice == 0:
            self.x += 1
        elif choice == 1:
            self.x -= 1
        elif choice == 2:
            self.y += 1
        else:
            self.y -= 1
    
    def diag_step(self):
        xstep = uniform(-1, 1)
        ystep = uniform(-1, 1)

        self.x += xstep
        self.y += ystep
    
    def biased_step(self):
        xstep = uniform(-0.5, 1)
        ystep = uniform(-1, 0.5)

        self.x += xstep
        self.y += ystep

    def dynamic_step(self):
        rnd = random()
        bias_x = mouse_x - self.x
        bias_y = mouse_y - self.y
        if rnd < 0.1:
            xstep = bias_x * 0.01
            ystep = bias_y * 0.01

        else:
            xstep = uniform(-1, 1)
            ystep = uniform(-1, 1)

        self.x += xstep
        self.y += ystep
    
    def gaussian_step(self):

        xstep =  gauss(0, 0.5)
        ystep = gauss(0, 0.5)

        self.x += xstep
        self.y += ystep

class PerlinWalker(object):

    def __init__(self):
        self.x = width / 2
        self.y = height / 2

        self.tx = 0
        self.ty = 10000

    def show(self):
        stroke(0)
        circle(self.x, self.y, 10)

    def step(self):

        self.x = interp(noise(self.tx),[0,1],[0, width])
        self.y = interp(noise(self.ty),[0,1],[0, height])

        self.tx += 0.01
        self.ty += 0.01
    
    def size_step(self):

        xstep = interp(noise(self.tx),[0,1],[-width / 100, width / 100])
        ystep = interp(noise(self.ty),[0,1],[-height / 100, height / 100])

        self.x += xstep
        self.y += ystep

        self.tx += 0.01
        self.ty += 0.01



