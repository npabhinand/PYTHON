from turtle import Turtle,Screen
import time
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
X_COR=360
screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()
is_on_game=True
scoreboard=Scoreboard()



    
screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")
while is_on_game:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)
    
    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor()<-280:
        ball.bounce_y()
    #Detect collision with paddle
    if ball.distance(r_paddle) < 40 and ball.xcor()>340 or ball.distance(l_paddle) < 40 and ball.xcor()<-340:
        ball.bounce_x()

    #Detect r
    if ball.xcor()>380:
        time.sleep(.1)
        ball.refresh()
        scoreboard.l_point()
    if ball.xcor()<-380:
        time.sleep(.1)
        ball.refresh()
        scoreboard.r_point()
    # if scoreboard.l_score=5 or 
        
        
        



screen.exitonclick()