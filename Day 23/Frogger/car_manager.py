import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
CAR_AMOUNT = 22

#turtle class to generate random cars

class CarManager(Turtle): # didn't need it to inherit the turtle class since it's not needed but too lazy to refactor it all as it works with what I have
    def __init__(self) -> None:
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1,stretch_len=2)
        self.color(random.choice(COLORS))
        self.pu()
        self.seth(180)
        self.goto((random.randrange(-180,800, 20)),(random.randrange(-240,260,20)))
        self.move_speed = STARTING_MOVE_DISTANCE
        self.car_list = []

    def move_car(self):        
        self.fd(self.move_speed)

    def restart(self):
        self.goto((random.randrange(310,800,20)),(random.randrange(-240,260,20)))
    
    def level_up(self,list):
        for _ in list:                
            _.move_speed += MOVE_INCREMENT

    def new_level(self):
        for _ in range(0,CAR_AMOUNT):
            new_car = CarManager()
            self.car_list.append(new_car)


