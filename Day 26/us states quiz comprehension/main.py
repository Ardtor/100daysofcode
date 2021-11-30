# US States guessing game using Turtle and CSV data
# Turtle will be used to display a map and prompt the user while the data will be used
# to check the users entry

import turtle
import pandas as pd

FONT = ("Courier", 8, "normal")
ALIGNMENT = "CENTER"

# sets up the screen
screen = turtle.Screen()
screen.screensize(canvheight=425, canvwidth=725)
screen.setup(width=750, height=500)
screen.tracer(0)
# sets up the turtle
state_image = turtle.Turtle()
image = "data/blank_states_img.gif"
# adds the shape in the form of the image
screen.addshape(image)
state_image.shape(image)

# Sets up the data from the CSV using Pandas as a dataframe
df = pd.read_csv("data/50_states.csv")
# Game variables
game_on = True
score = 0
correct_guesses = []
attempts_left = df.state.size

# main loop checks if the game is still on
while game_on is True and attempts_left > 0:
    screen.update()
    try:
        answer_state = screen.textinput(
            title=f"{len(correct_guesses)}/50 States Correct", prompt="Please enter a state: "
        ).title()
    except NameError:
        print("Please enter a state")
    # Uses an array from the data series to check if it matches the users guess, and isn't in the already guessed list
    if answer_state in df.state.array and answer_state not in correct_guesses:
        # creates a turtle and writes the name at the X,Y
        turtle.ht()
        turtle.pu()
        # sets up the X, Y that matches the correct answer_state
        turtle.goto(int(df[df.state == answer_state]["x"]), int(df[df.state == answer_state]["y"]))
        turtle.write(answer_state, align=ALIGNMENT, font=FONT)
        correct_guesses.append(answer_state)
        attempts_left -= 1
    elif answer_state in correct_guesses and not "":
        print("You've already entered this state correctly")
    elif answer_state == "":
        print("You need to enter something,try again")
    elif answer_state == "Exit":
        game_on == False
        # loops through the df.state array and checks to see if the missing ones are in the correct guess
        # if not they will append to the missing states list and then be written out as a CSV file

        # Day 26, removed the below for loop with a list comprehension 
        missing_states = [state for state in df.state.array if state not in correct_guesses]
        # for missing in df.state.array:
        #     if missing not in correct_guesses:
        #         missing_states.append(missing)
        pd.DataFrame(missing_states, columns=["State"]).to_csv("data/missing_states.csv", index=1)
        break
    else:
        print(f"You have {50-len(correct_guesses)} to guess and {attempts_left} attempts to go")
        attempts_left -= 1
    if attempts_left <= 0:
        print(f"Game over! You guessed {score} states correctly")
        game_on = False
