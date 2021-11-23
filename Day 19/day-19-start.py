# Listening to keyboard using turtle module, using events.

from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()
screen.listen() #sets up the screen object to listen for keybindings

def move_forwards():
    timmy.forward(10)


# This is the screen function in which we pass the function move_forwards over.
screen.onkey(key="space", fun=move_forwards)


#Exits on click, otherwise disappears
screen.exitonclick()