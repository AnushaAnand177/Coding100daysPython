import random
from turtle import Turtle, Screen


# Setup screen and turtle
screen = Screen()
screen.setup(width=1000, height=600)  # Set screen size
screen.bgcolor("white")
screen.colormode(255)


# Spirograph
spiro = Turtle()
spiro.shape("turtle")
screen.colormode(255)
spiro.speed(0)
spiro.width(2)

# random color function
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


# Spirograph function
def spirograph(tilt):
    """
    Draws a spirograph with the specified size_of_gap.

    The spirograph is drawn by repeatedly drawing a circle and then
    rotating the turtle by the specified angle, which is given by
    tilt.
    """
    for _ in range(int(360 / tilt)):
        # Set the turtle color to a random color
        spiro.color(random_color())
        # Draw a circle
        spiro.circle(100)
        # Rotate the turtle by the specified angle
        spiro.setheading(spiro.heading() + tilt)


spirograph(5)


screen.exitonclick()