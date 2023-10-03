from turtle import Turtle,Screen
import random
colors=[(246, 245, 243), (233, 239, 246), (246, 239, 242), (240, 246, 243), (132, 166, 205), (221, 148, 106), (32, 42, 61), 
       (199, 135, 148), (166, 58, 48), (141, 184, 162), (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71), 
       (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55), (156, 33, 31), (17, 97, 71), (52, 44, 49), (230, 161, 166), 
       (170, 188, 221), (57, 51, 48), (184, 103, 113), (32, 60, 109), (105, 126, 159), (175, 200, 188), (34, 151, 210), (65, 66, 56)]
t=Turtle()
screen=Screen()
screen.colormode(255)
num_of_dots=100
t.hideturtle()
for i in range(1,num_of_dots+1):
    t.dot(10,random.choice(colors))
    t.penup()
    t.forward(50)
    t.pendown()
    t.speed(0)
    if i%10==0:
        t.setheading(90)
        t.penup()
        t.forward(50)
        t.pendown()
        t.setheading(180)
        t.penup()
        t.forward(500)
        t.pendown()
        t.setheading(0)
    
screen.exitonclick()

