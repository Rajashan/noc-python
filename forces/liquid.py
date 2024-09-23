from p5 import *

class Liquid(object):

    def __init__(self, x, y, w, h, c):
        self.x = x
        self.y = y
        self.w = w
        self.h = h 

        self.c = c
    
    def show(self):
        no_stroke()
        fill(175)
        rect(self.x, self.y, self.w, self.h)
    
    def contains(self, mover):
        pos = mover.position

        return ((pos.x > self.x) & (pos.x < self.x + self.w) & (pos.y > self.y) & (pos.y < self.y + self.h))


    def calculate_drag(self, mover):

        speed = mover.velocity.copy().mag()

        drag_magnitude = self.c * speed * speed 

        drag_force = mover.velocity.copy()
        drag_force *= -1 

        drag_force = drag_force.normalize() * drag_magnitude

        return drag_force