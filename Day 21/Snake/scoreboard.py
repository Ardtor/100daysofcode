from turtle import Turtle

FONT = ("Courier",18,"normal")
ALIGNMENT = "CENTER"

class Scoreboard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.color("white")
        self.pu()
        self.goto(0,270)
        self.hideturtle()
        self.write_score()
        
        

    def update_score(self):
        self.clear()
        self.score += 1
        self.write_score()

    def write_score(self):
        self.write(f"Score : {self.score}",align=ALIGNMENT,font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER!",align=ALIGNMENT,font=FONT)

    
