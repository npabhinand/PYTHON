# from turtle import Turtle
# import random
# t=Turtle()
# colors=['red','blue','green','yellow','violet','black']
# num_sides=4
# while True:
#     t.color(random.choice(colors))
#     for _ in range(num_sides):
#         angle=360/num_sides
#         t.forward(100)
#         t.right(angle)
#     num_sides+=1
#     if num_sides==10:
#         break


##Another Maethod using function

from turtle import Turtle
import random 
t=Turtle()
colors=['red','blue','green','yellow','violet','black','indigo']
def draw_shape(num_sides):
    angle=360/num_sides
    for _ in range(num_sides):
        t.forward(100)
        t.right(angle)


for i in range(4,10):
    t.color(random.choice(colors))
    draw_shape(i)
    