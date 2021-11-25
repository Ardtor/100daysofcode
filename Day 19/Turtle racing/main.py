# Turtle racing project, 6 turtles race across the screen, create a class to allow multiple instances of the Turtle() object. Understand 'states' of a object
# The player can bet on the race, and each turtle is a colour of the rainbow (Red, orange, yellow, green, blue, indigo, violet)

from turtle import Turtle, Screen, getturtle
import random

screen = Screen()
# screen.listen() #sets up the screen object to listen for keybindings
screen.setup(width=500,height=400) # sets the height of the display screen in pixels
user_bet = screen.textinput(title="Who is the winner?", prompt="Which Turtle will win the race? Please pick a colour\nRed, orange, yellow, green, blue, indigo, violet").lower()
colours = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
all_turtles = []


def setup_turtles():
    alignment = -150
    
    for _ in colours:
        turtle_name = _ +'_turtle'
        turtle_name = Turtle(shape="turtle")
        turtle_name.color(_)
        turtle_name.pu()
        turtle_name.setposition(x=-235,y=alignment)
        alignment += 50
        all_turtles.append(turtle_name)


def race_turtles():
    random.shuffle(all_turtles) #shuffles the turtles to randomise the for loop
    is_race_on = False

    if user_bet:
        is_race_on = True #if the user hasn't made a bet then the race won't start

    while is_race_on:
        for turtle in all_turtles:
            if turtle.xcor() > 230: #checks to see if the turtle has hit the edge of the screen (the icon is 40x40 pixels and is only checked from the midway point)
                is_race_on = False # turns off the loop
                winner =  turtle.pencolor()
                if winner == user_bet:                        
                    print(f"You've bet correctly the winner was {str(winner).title()}")
                    break #added a break because sometimes the if statement completes before it terminates
                else:                       
                    print(f"You bet incorrectly, the winner was {str(winner).title()}")
                    break
                    
            rand_distance = random.randint(0,10) # for each loop it'll randomly move the turtle forward a distance
            turtle.forward(rand_distance)


setup_turtles()

race_turtles()










#Exits on click, otherwise disappears
screen.exitonclick()