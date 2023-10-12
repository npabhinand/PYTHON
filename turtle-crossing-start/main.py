import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
carManager=CarManager()
scoreboard=Scoreboard()
player=Player()
screen.listen()
screen.onkey(player.move_turtle,"Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    carManager.create_car()
    carManager.move_car()
    if player.ycor() > 300:
        scoreboard.update_level()
        player.refresh()
        carManager.level_up()
        scoreboard.increase_level()
    for car in carManager.all_cars:
        if car.distance(player)<20:
            scoreboard.game_over()
            game_is_on=False
        
        
screen.exitonclick()
