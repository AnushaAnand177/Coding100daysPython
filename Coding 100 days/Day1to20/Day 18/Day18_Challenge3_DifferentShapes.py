from turtle import Turtle, colormode

yuclid = Turtle()

# Set color mode to use RGB values from 0 to 255
colormode(255)


def draw_shapes(turtle, number_of_sides, r, g, b):
    if number_of_sides > 10:  # Base case: stop when sides are more than 9
        return
    angle = 360 / number_of_sides

    # Set the turtle's color using RGB values,ensuring the values wrap around if they exceed 255.
    turtle.color((r % 256, g % 256, b % 256))

    for _ in range(number_of_sides):
        turtle.forward(100)
        turtle.left(angle)

    # Increase the RGB values slightly for the next shape
    draw_shapes(turtle, number_of_sides + 1, r + 95, g + 80, b + 15)


# Start drawing from a triangle (3 sides) and an initial color (e.g., blue)
draw_shapes(yuclid, 3, 90, 80, 255)
