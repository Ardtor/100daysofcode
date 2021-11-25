from turtle import Turtle

FONT = ("Courier",18,"normal")
ALIGNMENT = "CENTER"

class Scoreboard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.score_p1 = 0
        self.score_p2 = 0
        self.color("white")
        self.pu()
        self.goto(0,270)
        self.hideturtle()
        self.write_score()
        
        

    def update_score(self,player):
        if player == 'p1':
            self.score_p1 += 1
        else: 
            self.score_p2 += 1
        self.clear()        
        self.write_score()

    def write_score(self):
        self.write(f"Score :\n P1:{self.score_p1}|P2:{self.score_p2}  ",align=ALIGNMENT,font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER!",align=ALIGNMENT,font=FONT)