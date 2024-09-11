from p5 import *

global x
global y

x = 100
y = 100

global xspeed
global yspeed
xspeed = 2.5
yspeed = 2

def setup():
    global x
    global y
    size(640, 240)

def draw():
    global x
    global y
    global xspeed
    global yspeed
    background(255)

    x += xspeed
    y += yspeed

    if (x > width or x < 0):
        xspeed = -xspeed
    if (y > height or y < 0):
        yspeed = -yspeed
    
    stroke(0)
    fill(127)
    circle(x, y, 48)

run()