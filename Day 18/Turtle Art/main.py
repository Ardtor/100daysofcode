# import colorgram
# from pathlib import Path
from turtle import Turtle, Screen
import random

timmy = Turtle() 
timmy.shape("turtle") #sets the turtle shape to 'turtle' but could basically be anything
screen = Screen()
screen.colormode(255)
screen.canvheight = 800
screen.canvwidth = 800
timmy.pu()

# p = Path.cwd()  / 'Day 18'/ 'Turtle Art'/ 'damienhirst.jpg'

# with p.open(mode='rb') as incoming:
#     colours = colorgram.extract(incoming,255) #this is returned as a list of named tuples

# colour_list = []

# for colour in colours: #runs through each one and creates a new tuple with only the values 
#     # r,g,b = colour.rgb.r, colour.rgb.g, colour.rgb.b
#     # new_colour = (r,g,b)
#     colour_list.append(tuple(colour.rgb)) #skips the above part by directly going to creating the tuple

# print(colour_list)


colour_list = [
    (226, 234, 243), (131, 164, 204), (228, 149, 99), (30, 44, 64), (245, 234, 238), (166, 58, 48), (202, 135, 147), (237, 212, 85), 
    (41, 101, 150), (135, 183, 161), (150, 62, 71), (52, 42, 45), (159, 33, 31), (219, 82, 73), (238, 165, 155), (58, 117, 99), 
    (60, 49, 45), (173, 29, 31), (231, 163, 168), (35, 61, 56), (15, 96, 71), (33, 60, 107), (170, 188, 222), (188, 101, 111), 
    (104, 126, 161), (14, 85, 109), (174, 200, 188), (33, 151, 211), (65, 66, 57), (100, 141, 129), (155, 202, 223), (143, 130, 108)
]

# Print 10 x 10 dots, 20 in size, 50 apart

def timmy_print(a,b):
    '''
    Takes two values, a and b. Which is the X, Y number of dots the user
    would like to use.
    
    '''
    timmy.speed(0)
    timmy.ht() #hides timmy    
    timmy.setpos(-400,-400) #sets pos to bottom left corner
    for _ in range(a):
        x,y = timmy.pos()
        if _ > 0:
            timmy.setpos((x - (b*50)),(y+50))
        
        for _ in range(b):                    
            timmy.dot(25,random.choice(colour_list))
            timmy.forward(50)
        

timmy_print(12,12)



screen.exitonclick()

