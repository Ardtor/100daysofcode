from turtle import Screen, position
from time import sleep
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black") # sets the background colour
screen.title("The Snake game") #sets the screen title
screen.listen() #sets up the screen object to listen for keybindings
screen.tracer(0) # disables automated screen refresh
game_on = True

snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.onkeypress(key="Up", fun=snake.move_up)
screen.onkeypress(key="Left", fun=snake.move_left)
screen.onkeypress(key="Down", fun=snake.move_down)
screen.onkeypress(key="Right", fun=snake.move_right)
# screen.onkeypress(key="r", fun=snake.add_onto_snake_2) #clears the drawings and reset to 0,0

while game_on:    
    screen.update() #updates the screen after each loop
    sleep(.1)  # sleeps for 0.25 seconds
    snake.move_snake()

    #food Collision 
    if snake.head.distance(food) <= 15:
        snake.add_onto_snake(1)
        scoreboard.update_score()
        food.spawn_food()
    
    #wall collision.

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or  snake.head.ycor() < -280: #checks if outside boundry
        game_on = False
        scoreboard.game_over()
        print("Out of bounds")

    #tall collision

    for seg in snake.segments: # runs through each segment 
        if seg == snake.head: #ignores the segment if it's snake.head
            pass
        elif snake.head.distance(seg) < 10: # else if the distance is less than 10 heading for a tail strike
            game_on = False
            scoreboard.game_over()
            print("Tail strike")


    


#Exits on click, otherwise disappears
screen.exitonclick()