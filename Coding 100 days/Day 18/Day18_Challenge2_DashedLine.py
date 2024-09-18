import turtle

# create a square

turtle.shape("turtle")
turtle.color("red")
for _ in range(51):
    turtle.forward(10)
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()