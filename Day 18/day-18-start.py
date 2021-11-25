from turtle import Screen, Turtle
import random
# import turtle as t is also valid  so it will be t.whatever 

# available colours = https://cs111.wellesley.edu/labs/lab01/colors

timmy = Turtle() 
timmy.shape("turtle") #sets the turtle shape to 'turtle' but could basically be anything
screen = Screen()
screen.colormode(255)

################
# Challenge #1#
###############

# Draw a square
# for _ in range(4):
#     timmy.fd(100)
#     timmy.rt(90)

###############
#Challenge #2 #
###############


# Draw a dotted line
# for _ in range (20):
#     timmy.pd()
#     timmy.fd(10)
#     timmy.up()
#     timmy.fd(10)

##############
# Challenge 3#
##############

# Draw various shapes - 360 degrees / number of sides

# def draw_timmy(b): # takes in the range of the objects you want to use
#     '''
#     Enter the largest object you'd like the turtle to draw as a number of sides i.e triangle is 3
#     '''
#     
#     for sides in range(3,b+1):
#         side_count = sides
#         timmy.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
#         for _ in range(side_count):        
#             timmy.forward(100)
#             timmy.rt(360/side_count)

# draw_timmy(3)

##########################################
# Challenge 4 take Timmy on a random walk#
##########################################

def random_timmy(num):
    '''
    Sends timmy on a random walk for num times. 
    Will hide timmy and let him roam randomly across the canvas, each loop will change his colour
    '''
    timmy.speed(0)
    direction = [0,90,180,270]
    timmy.pensize(20)
    timmy.ht()
    for i in range(num):
        timmy.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))    
        timmy.seth(random.choice(direction))
        timmy.forward(50)
        # timmyx,timmyy = timmy.pos()
        
        # if timmyx and timmyy > 400 or timmyx and timmyy < -400:
        #     timmy.pu()
        #     timmy.home()
        #     timmy.pd()


def spirograph_timmy(size):
    '''
    takes in the size of the spacing the user would like and then prints enough
    circles to make a 360 degree spirograph
    '''
    timmy.speed(0)
    timmy.ht()
    start_angle = 0
    for _ in range (int(360/size)):        
        timmy.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        timmy.seth(start_angle)
        timmy.circle(200)
        start_angle += size

spirograph_timmy(8)






























# This needs to be at the end to stop the screen/canvas from exiting. 
screen.exitonclick()

