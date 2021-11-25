from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,coords):
        super().__init__()
        self.speed(0)
        self.color("white")
        self.shape("square")
        self.pu()
        self.shapesize(stretch_len=5,stretch_wid=1)
        self.seth(90)
        self.goto(coords)                 

    def move_up(self):
        if self.ycor() > 220:
            pass
        else:
            self.fd(20)

    def move_down(self):
        if self.ycor() < -220:
            pass
        else:
            self.back(20)





