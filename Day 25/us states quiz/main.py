# US States guessing game using Turtle and CSV data
# Turtle will be used to display a map and prompt the user while the data will be used
# to check the users entry

import turtle
import pandas as pd

FONT = ("Courier", 8, "normal")
ALIGNMENT = "CENTER"

screen = turtle.Screen()
screen.screensize(canvheight=425, canvwidth=725)
screen.setup(width=750, height=500)
screen.tracer(0)
state_image = turtle.Turtle()
image = "data/blank_states_img.gif"
screen.addshape(image)
state_image.shape(image)
state_image.shapesize(stretch_len=2, stretch_wid=2)

# answer_state = screen.textinput(title="Enter a guess", prompt="Please enter a state: ").title()

df = pd.read_csv("data/50_states.csv")
game_on = True
score = 0
correct_guesses = []
attempts_left = df.state.size

while game_on:
    screen.update()
    try:
        answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="Please enter a state: ").title()
    except NameError:
        print("Please enter a state")
    # if answer_state in df.state.values and answer_state not in correct_guesses:
    if answer_state in df.state.array and answer_state not in correct_guesses:
        turtle.ht()
        x = int(df[df.state == answer_state]["x"])
        y = int(df[df.state == answer_state]["y"])
        turtle.pu()
        turtle.goto(x, y)
        turtle.write(answer_state, align=ALIGNMENT, font=FONT)
        score += 1
        correct_guesses.append(answer_state)
        attempts_left -= 1
    elif answer_state in correct_guesses and not "":
        print("You've already entered this state correctly")
    else:
        print(f"You have {50-score} to guess and {attempts_left} attempts to go")
        attempts_left -= 1


# Required to exit
# turtle.mainloop()
screen.exitonclick()
