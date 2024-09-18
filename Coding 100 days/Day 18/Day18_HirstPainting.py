import random
import colorgram
from turtle import Turtle, Screen

screen = Screen()
colors = colorgram.extract("C:\\Users\\anush\\Downloads\\hirst spot painting.jpg", 30)
screen.colormode(255)
turtle = Turtle()
turtle.speed(3)

rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r, g, b))

#Function to draw spots
def draw_spots(lines):
    turtle.hideturtle()
    turtle.penup()
    turtle.setheading(225)
    turtle.forward(300)
    turtle.setheading(0)
    for _ in range(lines):
        for _ in range(10):
            turtle.dot(20, random.choice(rgb_colors))
            turtle.forward(50)
        turtle.backward(500)
        turtle.left(90)
        turtle.forward(50)
        turtle.right(90)


draw_spots(10)

screen.exitonclick()