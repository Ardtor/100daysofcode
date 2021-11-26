import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

#Sets up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

#sets up objects

player = Player()
score_board = Scoreboard()
car_manager = CarManager()
car_list = car_manager.car_list

#setup key presses
screen.onkeypress(key="w", fun=player.move_forward)

#main loop

def main():
    game_is_on = True 
    car_manager.new_level() #generates the level from a ranged list
    while game_is_on:
        time.sleep(0.1)
        screen.update()        

        # loop through all the cars and check if they're off screen if so reset their position to a random range off screen
        # Checks to see if the user is within distance to be a game over
        # Otherwise it'll move them forward 
        for _ in car_list:
            if _.xcor() < -300:
                _.restart()
            elif _.distance(player) < 20:
                score_board.game_over()
                game_is_on = False
            else:
                _.move_car()        
        
        # Checks if the user has reached above a Y-Co-ord if so it'll return true then update the scoreboard and loop through the
        # car_list and update it

        if  player.player_reset() == True:
            score_board.update_score()
            car_manager.level_up(car_list)



main()







# Should always be the last line or the screen will exit randomly
screen.exitonclick()
