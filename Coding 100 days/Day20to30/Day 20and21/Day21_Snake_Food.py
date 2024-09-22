import random
from turtle import Turtle,Screen

class Food(Turtle):
    def __init__(self):
        """
        Initializes the class instance.

        This method sets up the initial properties of the shape object.

        Actions performed:
        - Sets the shape to 'circle'.
        - Adjusts the size of the turtle to a smaller scale.
        - Changes the color of the shape to blue.
        - Lifts the pen, so it won't draw when it's moved.
        - Moves the turtle object to coordinates (60, 40).
        """
        super().__init__()
        self.shape("circle")
        self.turtlesize(0.5, 0.5)
        self.color("blue")
        self.penup()
        self.goto(60 , 40)

    def food_position(self):
        """
        Calculate a random position within the range (-280, 280) for both x and y coordinates
        and set the object's position to these coordinates.

        :return: None
        """
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.setpos(random_x, random_y)




