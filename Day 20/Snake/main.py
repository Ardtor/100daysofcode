from turtle import Turtle, Screen
from time import sleep

# turtle has 0 as EAST

starting_segment = Turtle(shape="square")
starting_segment.color("white")
starting_segment.pu()


screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black") # sets the background colour
screen.title("The Snake game") #sets the screen title
screen.listen() #sets up the screen object to listen for keybindings
screen.tracer(0) # disables automated screen refresh
segments = [starting_segment,]
game_on = True

def add_onto_snake(number):
    for num in range(number):
        segment = Turtle(shape="square")
        segment.color("white")
        segment.pu()
        new_position_x = int(segments[0].xcor()-(20*(num+1)))
        new_position_y = int(segments[0].ycor())
        segment.setposition(x=new_position_x,y=new_position_y)
        segments.append(segment)

add_onto_snake(2)


while game_on:
    screen.update() #updates the screen after each loop
    sleep(.250)  # sleeps for 0.25 seconds
    
    for seg_num in range(len(segments)-1, 0, -1): #range needs to start at last segment then go through each one to move them to the last place, start,stop,step (-1 is reverse)
        new_x,new_y = segments[seg_num -1].pos() #takes the tuple from pos and returns it
        segments[seg_num].goto(new_x,new_y)
    segments[0].forward(20)






#Exits on click, otherwise disappears
screen.exitonclick()