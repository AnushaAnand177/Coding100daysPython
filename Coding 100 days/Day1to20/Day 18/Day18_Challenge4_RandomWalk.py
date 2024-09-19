from turtle import Turtle, Screen
import random

# Setup screen and turtle
screen = Screen()
screen.setup(width=1000, height=600)  # Set screen size
screen.bgcolor("white")
screen.colormode(255)

percy = Turtle()
percy.width(10)
percy.speed(10)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colour = (r, g, b)
    return random_colour


# Function to check if turtle is inside the screen boundaries
def is_in_bounds(turtle, screen_width, screen_height):
    """
    Check if turtle is inside the screen boundaries.

    Args:
        turtle (Turtle): Turtle object.
        screen_width (int): Width of the screen.
        screen_height (int): Height of the screen.

    Returns:
        bool: True if inside bounds, False otherwise.
    """
    x, y = turtle.position()
    # Calculate half of the screen width and height
    half_width = screen_width / 2
    half_height = screen_height / 2
    # Check if turtle is inside the screen boundaries
    return -half_width < x < half_width and -half_height < y < half_height

# Get screen width and height
screen_width = screen.window_width()
screen_height = screen.window_height()

for _ in range(200):
    percy.forward(20)

    # Check if percy is going out of bounds
    if not is_in_bounds(percy, screen_width, screen_height):
        percy.setheading(random.choice(
            [0, 90, 180, 270]))  # Move it in a random direction if it's near the edge
    else:
        percy.setheading(random.randint(0, 360))  # Otherwise move to any random angle

    percy.color(random_color())

screen.exitonclick()


