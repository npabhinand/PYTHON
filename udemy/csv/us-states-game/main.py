import turtle
import pandas
screen=turtle.Screen()
screen.title("US State Game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guessed_state=[]
missing_states=[]
data=pandas.read_csv("50_states.csv")
all_states=data['state'].to_list()
game_is_on=True
score=0
while game_is_on:
    answer_state=screen.textinput(title=f"{score}/{len(all_states)}",prompt="What's another state name is").title()
    if answer_state in all_states:
        guessed_state.append(answer_state)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data.state==answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer_state)
        score+=1
    if answer_state=="Exit":
        for state in all_states:
            if state not in guessed_state:
                missing_states.append(state)
        new_data=pandas.DataFrame(missing_states)
        new_data.to_csv("Missing states.csv")
        game_is_on=False
        
        
        

turtle.exitonclick()

