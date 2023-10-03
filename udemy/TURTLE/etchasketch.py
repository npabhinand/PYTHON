from turtle import Turtle,Screen

screen=Screen()
t=Turtle()
def move_forward():
    t.forward(10)
def move_backward():
    t.backward(10)
def move_left():
    new_heading=t.heading()+10
    t.setheading(new_heading)
def move_right():
    new_heading=t.heading()-10
    t.setheading(new_heading)
def reset_screen():
    t.reset()
screen.listen()
screen.onkey(move_forward,"w")
screen.onkey(move_backward,"s")
screen.onkey(move_left,"a")
screen.onkey(move_right,"d")
screen.onkey(reset_screen,"c")
screen.exitonclick()
            