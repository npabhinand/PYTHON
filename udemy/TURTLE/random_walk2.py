from turtle import Turtle, Screen
import random

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    colors= (r,g,b)
    return colors

t=Turtle()
screen = Screen()
screen.colormode(255)
direction=[0,90,180,270]
t.pensize(10)
t.speed(10)

for _ in range(1000):
    t.color(random_color())
    t.forward(20)
    t.setheading(random.choice(direction))
   