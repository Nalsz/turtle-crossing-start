from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.allcars = []
        self.speed = 5

    def create_cars(self):
        choice = random.randint(1, 6)
        if choice == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_y = random.randint(-250, 250)
            new_car.penup()
            new_car.goto(300, new_y)
            self.allcars.append(new_car)

    def move_car(self):
        for car in self.allcars:
            car.backward(self.speed)

    def increase_speed(self):
        self.speed += MOVE_INCREMENT
