from turtle import Turtle,Screen
import random
screen=Screen()
screen.setup(width=500,height=400)
colors=["red","green","purple","yellow","blue","orange"]
turtle_list=[]
y_cordinates=[-90,-60,-30,0,30,60]
user_bet=screen.textinput("Make your bet","Which turtle win the race")
for i in range(0,6):
    new_turtle=Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(-230,y_cordinates[i])
    turtle_list.append(new_turtle)
if user_bet:
    start=True
while start:
    for turtle in turtle_list:
        if turtle.xcor()>230:
            start=False
            winning_color=turtle.pencolor()
            if user_bet==winning_color:
                print(f"You've won the match. The winner is {winning_color} turtle")
            else:
                print(f"You've lost the match. The winner is {winning_color} turtle")
        random_walk=random.randint(0,10)
        turtle.forward(random_walk)
screen.exitonclick()