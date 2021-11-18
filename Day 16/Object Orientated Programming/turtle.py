from turtle import Turtle, Screen
import turtle # Turtle is a old school gfx module

# https://cs111.wellesley.edu/labs/lab01/colors colors for timmy
# https://docs.python.org/3/library/turtle.html


timmy = Turtle() # creates an object of the turtle class, as it's upper/pascal case LikeThisIsPascal
timmy.shape("turtle")

timmy.color("firebrick2")

timmy.up()
timmy.goto(100,0)
# Makes timmy draw a square.
# timmy.fd(300)
# timmy.rt(90)
# timmy.fd(300)
# timmy.rt(90)
# timmy.fd(300)
# timmy.rt(90)
# timmy.fd(300)
# timmy.rt(90)
# timmy.fd(300)



my_screen = Screen() #screen is the display that canvas that the turtle will draw on

print(my_screen.canvheight) # calls the canvheight method to return it's height.

my_screen.exitonclick() #only exits the canvas when the mouse is clicked



