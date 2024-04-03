import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

playa = Player()
car_manager = CarManager()
sb = Scoreboard()

screen.onkey(playa.move, "Up")

level=1

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars(level)
    if playa.ycor() > 280:
        playa.go_home()
        sb.level_up()
        car_manager.level_up()
    for car in car_manager.cars:
        if car.distance(playa) < 20:
            game_is_on = False


screen.exitonclick()
