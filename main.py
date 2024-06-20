import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.listen()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move_car()

    # Detect collision with car
    for car in car_manager.allcars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect when player is at finish line
    if player.is_at_finish_line():
        player.return_to_starting_position()
        car_manager.increase_speed()
        scoreboard.update_level()

screen.exitonclick()
