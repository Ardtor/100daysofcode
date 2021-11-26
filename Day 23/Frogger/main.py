import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# placed everything in main so we can restart it via dialog box


def main():
    # Sets up the screen
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)
    screen.listen()

    # sets up objects

    player = Player()
    score_board = Scoreboard()
    car_manager = CarManager()
    car_list = car_manager.car_list

    # setup key presses
    screen.onkeypress(key="w", fun=player.move_forward)

    # main loop
    game_is_on = True
    car_manager.new_level()  # generates the level from a ranged list

    while game_is_on:
        time.sleep(0.1)
        screen.update()
        # Checks to see if the user is within distance to be a game over
        # Otherwise it'll move the cars forward
        for car in car_list:
            if car.distance(player) < 20:
                score_board.game_over()
                retry = screen.textinput("Try again?", "Would you like to try again? Y or N").lower()
                if retry == "y":
                    screen.clearscreen()
                    main()
                else:
                    game_is_on = False
                    break
        car_manager.move_car()

        # Checks if the user has reached above a Y Coord if so it'll return true then update the scoreboard and increase the speed
        if player.player_reset() == True:
            score_board.update_score()
            car_manager.level_up()

    # Should always be the last line or the screen will exit randomly
    screen.exitonclick()


main()
