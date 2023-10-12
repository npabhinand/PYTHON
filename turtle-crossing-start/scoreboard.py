from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGNMENT="center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        # self.color("white")
        self.penup()
        self.level=1
        self.hideturtle()
        self.update_level()
    def update_level(self):
        self.clear()
        self.goto(200,250)
        self.write(f"level-{self.level}",align=ALIGNMENT,font=FONT)
    def increase_level(self):
        self.level+=1
        self.update_level()
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over",align=ALIGNMENT,font=FONT)
        
        
        
