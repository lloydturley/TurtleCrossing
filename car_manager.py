from turtle import Turtle
import random, time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.car_speed = STARTING_MOVE_DISTANCE
        self.cars = []

    def create_car(self):
        if random.randint(0,10)==1:
            tur = Turtle()
            tur.color(COLORS[random.randint(0,5)])
            tur.penup()
            tur.goto(280, random.randint(-260, 260))
            tur.shape("square")
            tur.setheading(180)
            tur.shapesize(stretch_wid=1, stretch_len=2)
            self.cars.append(tur)

    def move_cars(self, level=1):
        for car in self.cars:
            # time.sleep(0.1)
            car.forward(self.car_speed)
            if car.xcor()<-280:
                car.goto(300, random.randint(-250, 250))

    def level_up(self):
        self.car_speed+=MOVE_INCREMENT