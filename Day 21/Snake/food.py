from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.pu()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("blue")
        self.speed(0)
        self.spawn_food()
        
        
    def spawn_food(self):
        random_x = random.randrange(-260,260,20)
        random_y = random.randrange(-260,260,20)
        self.goto(random_x, random_y)

