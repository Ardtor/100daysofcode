from turtle import Screen
from time import sleep
from paddles import Paddle
from ball import Ball
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black") # sets the background colour
screen.title("Pong") #sets the screen title
screen.listen() #sets up the screen object to listen for keybindings
screen.tracer(0) # disables automated screen refresh
game_on = True
speed = 0.05 #game speed
position = True

#Creates paddles
l_paddle = Paddle((-350,0))
r_paddle = Paddle( (350,0))
#Sets up ball
ball = Ball()
scoreboard = Scoreboard()

#sets up keys 
screen.onkeypress(key="Up", fun=r_paddle.move_up)
screen.onkeypress(key="Down", fun=r_paddle.move_down)
screen.onkeypress(key="w", fun=l_paddle.move_up)
screen.onkeypress(key="s", fun=l_paddle.move_down)

#main loop
while game_on:
    screen.update() #updates the screen after each loop
    sleep(speed)
    ball.ball_move()
    # print(f"Left = {ball.distance(l_paddle)}, Right ={ball.distance(r_paddle)}")
    if scoreboard.score_p1 >= 10 or scoreboard.score_p2 >= 10:
        game_on = False
        scoreboard.game_over()

    #detects if the ball is within 50 units of the paddle and past 320 to stop the turtle from sinking into the other one
    if ball.distance(l_paddle) <= 50 and ball.xcor() <= -320 or ball.distance(r_paddle) <= 50 and ball.xcor() >= 320:
        ball.bat_detection()
    
    #checks if the ball goes close to these values bounce the ball back by inverting the direction
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball_heading = -ball.heading()
        ball.seth(ball_heading)

    #scoring if it goes past the paddles
    if ball.xcor() >= 380:
        scoreboard.update_score('p1')
        ball.ball_reset()

    elif ball.xcor() <= -380:
        scoreboard.update_score('p2')
        ball.ball_reset()

        



#Exits on click, otherwise disappears
screen.exitonclick()