import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
CAR_AMOUNT = 28

# turtle class to generate random cars
class CarManager:  # refactored it because it bugged me 15 minutes after realising
    def __init__(self) -> None:
        self.car_list = []
        self.move_speed = STARTING_MOVE_DISTANCE

    def move_car(self):
        for car in self.car_list:
            if car.xcor() < -300:
                car.goto((random.randrange(310, 800, 20)), (random.randrange(-240, 260, 20)))
            car.fd(self.move_speed)

    def level_up(self):
        self.move_speed += MOVE_INCREMENT

    def new_level(self):
        for _ in range(0, CAR_AMOUNT):
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.pu()
            new_car.seth(180)
            new_car.goto((random.randrange(-180, 800, 20)), (random.randrange(-240, 260, 20)))
            self.car_list.append(new_car)
