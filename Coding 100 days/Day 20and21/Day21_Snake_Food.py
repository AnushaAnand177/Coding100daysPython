import random
from turtle import Turtle,Screen

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.turtlesize(0.5, 0.5)
        self.color("blue")
        self.penup()
        self.goto(60 , 40)

    def food_position(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.setpos(random_x, random_y)




