from p5 import *
from random import random, randrange
from numpy import interp

class Mover(object):
    def __init__(self):
        self.position = Vector(random() * width, random() * height)
        self.velocity = Vector(0, 0)
        self.acceleration = Vector(0, 0)

        self.top_speed = 20
        self.tx = 1
        self.ty = 0.001
    
    def update(self):
        self.acceleration = Vector.random_2D()
        self.acceleration *= random() * 2
        self.velocity += self.acceleration
        self.velocity.limit(self.top_speed)
        self.position += self.velocity
    
    def perlin_update(self):
        self.acceleration.x += noise(self.tx)
        self.acceleration.y += noise(self.ty)

        self.tx += 0.01
        self.ty += 0.01

        self.velocity += self.acceleration
        self.velocity.limit(self.top_speed)
        self.position += self.velocity
    
    def update_mouse(self):
        mouse = Vector(mouse_x, mouse_y)
        dir = mouse - self.position

        #dir.normalize()

        inc = float(1/dir.mag())
        print(inc)

        dir *= inc

        self.acceleration = dir
        self.velocity += self.acceleration
        self.velocity.limit(self.top_speed)
        self.position += self.velocity
    
    def show(self):
        stroke(0)
        fill(175)

        circle(self.position.x, self.position.y, 48)
    
    def check_edges(self):

        if self.position.x > width:
            self.position.x = 0
        elif self.position.x < 0:
            self.position.x = width
        
        if self.position.y > height:
            self.position.y = 0
        elif self.position.y < 0:
            self.position.y = height

    def limit(self, max):
        if self.mag() > max:
            self.normalize()
            self *= max