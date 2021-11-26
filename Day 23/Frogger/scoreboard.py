from turtle import Turtle

ALIGNMENT = 'left'
FONT = ("Courier", 18, "normal")

# Has the level and will print game over.

class Scoreboard(Turtle):
        def __init__(self) -> None:
            super().__init__()
            self.level = 1
            self.color("black")
            self.pu()
            self.goto(-270,270)
            self.hideturtle()
            self.write_score()
        
        def update_score(self):
            self.level += 1
            self.clear()        
            self.write_score()

        def write_score(self):
            self.write(f"Level: {self.level}  ",align=ALIGNMENT,font=FONT)

        def game_over(self):
            self.goto(-75,0)
            self.write(f"GAME OVER!",align=ALIGNMENT,font=FONT)
            
