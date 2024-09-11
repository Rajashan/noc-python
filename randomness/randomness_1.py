from p5 import *
from random import choice


total = 20

random_counts = [0] * total

def setup():
    size(640, 240)

def draw():
    background(255)
    index = choice(range(total ))
    random_counts[index] += 1

    stroke(0)
    fill(127)

    w = width / len(random_counts)

    for x in range(len(random_counts)):
        rect(x * w, height - random_counts[x], w - 1, random_counts[x])

run()