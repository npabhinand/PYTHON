# from turtle import *

# # for steps in range(100):
# #     for c in ('green','red','yellow'):
# #         color(c)
# #         forward(steps)
# #         left(90)

# while True:
#     forward(100)
#     left(90)
#     color('red')
#     end_fill()

from turtle import Turtle
t=Turtle()
t.screen.bgcolor('green')
t.screen.title('square')
for i in range(12):
    t.color('black')
    t.forward(200)
    t.right(90)
