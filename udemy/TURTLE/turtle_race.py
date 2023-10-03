from turtle import Turtle,Screen
import random

screen=Screen()
screen.setup(width=500,height=400)
user_bet=screen.textinput("Make your bet","Which turtle win the race")
colors=["red","orange","yellow","green","blue","purple"]
y_positions=[-70,-40,-10,20,50,80]
all_turtles=[]
for i in range(0,6):
    new_turtle=Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-240,y=y_positions[i])
    all_turtles.append(new_turtle)
if user_bet:
    is_race_on=True
while is_race_on: 
    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on=False
            winning_color=turtle.pencolor()
            if user_bet==winning_color:
                print(f"You've won! The {winning_color} turtle is winner")
            else:
                print(f"you've loss! The {winning_color} turtle is winner")
            break
        rand_distance=random.randint(0,10)
        turtle.forward(rand_distance)
        

screen.exitonclick()