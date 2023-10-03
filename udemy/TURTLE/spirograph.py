from turtle import Turtle,Screen;
import random
t=Turtle()
screen=Screen()
screen.colormode(255)
t.speed(0)
def color_pick():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    colors=(r,g,b)
    return colors
for _ in range(100):
    t.circle(100)
    t.right(5)
    t.color(color_pick())

screen.exitonclick()

