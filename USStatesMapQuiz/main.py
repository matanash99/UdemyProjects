import turtle

import pandas as pd

screen = turtle.Screen()
screen.title("U.S States Game")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# def get_mouse_click(x,y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click)
# turtle.mainloop()
score = 0

guessed_states = []

data = pd.read_csv("50_states.csv")
states = data["state"].to_list()

while score < 50:
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another another state's name?").title()

    if answer_state == "Exit":

        missing_states = [state for state in states if state not in guessed_states]
        to_learn = pd.DataFrame(missing_states)
        to_learn.to_csv("states_to_learn.csv")
        break

    if answer_state in states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())
        score += 1
