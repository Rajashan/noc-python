from p5 import *

class Mover(object):
    def __init__(self, x, y, mass):
        self.position = Vector(x, y)
        self.velocity = Vector(0, 0)
        self.acceleration = Vector(0, 0)
        self.mass = mass
        self.radius = self.mass * 8
    
    def apply_force(self, force):
        f = force.copy()
        f = f / self.mass
        self.acceleration += f
    
    def update(self):
        self.velocity += self.acceleration
        self.position += self.velocity

        self.acceleration *= 0

    def check_edges(self):

        if (self.position.x < 0 + self.radius or self.position.x > width - self.radius):
            self.velocity = -self.velocity
        if (self.position.y < 0 + self.radius or self.position.y > height - self.radius):
            self.velocity = -self.velocity
    
    def show(self):

        stroke(0)
        fill(175)

        circle(self.position.x, self.position.y, self.mass * 16)
    
    def contact_edge(self):
        return (self.position.y > height - self.radius - 1)
    
    def bounce_edges(self):
        bounce = -0.9

        if (self.position.y > height - self.radius):
            self.position.y = height - self.radius
            self.velocity.y *= bounce
    
    def distance_nearest_edge(self):

        dist_up = self.position.y
        dist_down = height - self.position.y
        dist_left = self.position.x
        dist_right = width - self.position.x

        min_dist = min(dist_up, dist_down, dist_left, dist_right)

        if min_dist == dist_up:
            shortest = ("up", min_dist)
        elif min_dist == dist_down:
            shortest = ("down", min_dist)
        elif min_dist == dist_left:
            shortest = ("left", min_dist)
        elif min_dist == dist_right:
            shortest = ("right", min_dist)
        
        return shortest

    def calculate_friction(self):
        
        self.c = self.mass * 0.1
        friction = self.velocity.copy()
        friction *= -1
        friction = friction.normalize() * self.c

        return self.friction



    

