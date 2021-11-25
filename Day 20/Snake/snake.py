from turtle import Turtle

MOVE_DISTANCE = 20
UP, DOWN, LEFT, RIGHT = 90,270,180,0 # Angles for the turtle


# turtle has 0 as EAST
class Snake():
    def __init__(self) -> None:        
        starting_segment = Turtle(shape="square")
        starting_segment.color("white")
        starting_segment.pu()
        starting_segment.speed(1)
        self.segments = [starting_segment,]
        self.head = self.segments[0]
        self.add_onto_snake(2)   
    

    def add_onto_snake(self,num):
        for num in range(num):
            segment = Turtle(shape="square")
            segment.color("white")
            segment.pu()
            segment.speed(1)
            new_position_x = int(self.segments[-1].xcor()-(20*(num+1)))
            new_position_y = int(self.segments[-1].ycor())
            segment.setposition(x=new_position_x,y=new_position_y)
            self.segments.append(segment)

    def move_snake(self):
        for seg_num in range(len(self.segments)-1, 0, -1): #range needs to start at last segment then go through each one to move them to the last place, start,stop,step (-1 is reverse)
            new_x,new_y = self.segments[seg_num -1].pos() #takes the tuple from pos and returns it
            self.segments[seg_num].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)
    
    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)    

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)
    






