from turtle import Turtle

FONT = ("Courier", 18, "normal")
ALIGNMENT = "CENTER"
# HIGHSCORE_PATH = "Day 24\Snake_v2\highscore.txt" # had trouble with VS Code for some reason ignoring the CWD in Debug mode.
HIGHSCORE_PATH = "highscore.txt" 
# fixed it! needed 
# "cwd": "${fileDirname}",
# in the launch.json for debugging


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        # self.highscore = 0
        self.color("white")
        self.pu()
        self.goto(0, 270)
        self.hideturtle()
        self.read_highscore()
        self.write_score()

    # Day 24 - Reads the high score, and assigns it to self.highscore
    def read_highscore(self):
        with open(HIGHSCORE_PATH) as f:
            self.highscore = int(f.read())

    def update_score(self):
        self.score += 1
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score : {self.score} | High score:{self.highscore}", align=ALIGNMENT, font=FONT)

    # Updated from Day 22, to save the highscore compares
    # the current to the previous, if higher writes to the file

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open(HIGHSCORE_PATH, "w") as f:
                f.write(str(self.highscore))
        self.score = 0
        self.write_score()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER!",align=ALIGNMENT,font=FONT)
