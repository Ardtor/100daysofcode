from turtle import Turtle
import random

# width 20, height 20, x & y is 0.
# Moves 45 degress east on screen refresh.

class Ball(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.speed(0)
        self.color("white")
        self.shape("circle")
        self.pu()
        self.seth(145)
        
    
    def ball_move(self):        
        self.fd(15)

    def bat_detection(self):
        ball_heading = -self.heading()
        self.seth(ball_heading + 180)

    def ball_reset(self):
        self.goto(0,0)
        ball_heading = self.heading() + 180 + random.randint(0,70)
        self.seth(ball_heading)


            


