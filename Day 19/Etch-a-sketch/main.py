# Create an etch-a-sketch, with wasd movement and C to clear the screen

from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()
screen.listen() #sets up the screen object to listen for keybindings



def move_forwards():
    timmy.forward(10)
    

def move_left():
    timmy.left(10)

def move_right():
    timmy.right(10)

def move_back():
    timmy.back(10)


# This is the screen function in which we pass the function move_forwards over.

screen.onkeypress(key="w", fun=move_forwards)
screen.onkeypress(key="a", fun=move_left)
screen.onkeypress(key="s", fun=move_back)
screen.onkeypress(key="d", fun=move_right)
screen.onkeypress(key="c", fun=timmy.reset) #clears the drawings and reset to 0,0











#Exits on click, otherwise disappears
screen.exitonclick()