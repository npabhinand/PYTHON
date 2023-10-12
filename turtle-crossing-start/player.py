from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.shapesize(stretch_len=1,stretch_wid=1)
        self.penup()
        self.refresh()
        self.move_turtle()
        self.setheading(90)
    def refresh(self):
        self.goto(STARTING_POSITION)
    def move_turtle(self):
        new_y= self.ycor()+MOVE_DISTANCE
        self.goto(self.xcor(),new_y)
        
