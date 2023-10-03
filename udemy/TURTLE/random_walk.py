from turtle import Turtle
import random
t=Turtle()
t.pensize(10)
t.speed(10)
colors=['silver','black','cornflower blue','midnight blue','powder blue','cyan','sea green','dark green','gold',
        'sienna','maroon','chocolate','crimson','magenta','indigo','dark violet']
direction=[0,90,180,270]
for _ in range(1000):
    t.forward(20)
    t.setheading(random.choice(direction))
    t.color(random.choice(colors))