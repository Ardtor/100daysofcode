from turtle import Screen
from time import sleep
from snake import Snake

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black") # sets the background colour
screen.title("The Snake game") #sets the screen title
screen.listen() #sets up the screen object to listen for keybindings
screen.tracer(0) # disables automated screen refresh
screen.delay(0)
game_on = True

snake = Snake()


screen.onkeypress(key="Up", fun=snake.move_up)
screen.onkeypress(key="Left", fun=snake.move_left)
screen.onkeypress(key="Down", fun=snake.move_down)
screen.onkeypress(key="Right", fun=snake.move_right)
# screen.onkeypress(key="r", fun=snake.add_onto_snake_2) #clears the drawings and reset to 0,0

while game_on:    
    screen.update() #updates the screen after each loop
    sleep(.1)  # sleeps for 0.25 seconds        
    
    snake.move_snake()
    


#Exits on click, otherwise disappears
screen.exitonclick()