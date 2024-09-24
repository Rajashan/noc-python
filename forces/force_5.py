from p5 import *
from body import Body
from random import random

def setup():
    size(640, 360)
    global bodies
    global G 

    bodies = []

    for i in range(10):
        bodies.append(Body(random() * width, random() * height, random() * 5))
                      
    G = 1.0

def draw():
    background(255)

    for i in range(len(bodies)):
        for j in range(len(bodies)):
            if i != j:
                force = bodies[j].attract(bodies[i])
                bodies[i].apply_force(force)
                
            
        bodies[i].update()
        bodies[i].show()

run()