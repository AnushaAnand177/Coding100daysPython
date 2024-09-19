import turtle

# Set up screen
screen = turtle.Screen()
screen.title("Turtle Event Listener Example")
screen.setup(width=600, height=600)

# Create a turtle object
dusty = turtle.Turtle()
dusty.shape("turtle")
dusty.speed(1)

# Define callback functions
def move_forward():
    dusty.forward(50)

def move_backward():
    dusty.backward(50)

def turn_left():
    dusty.setheading(dusty.heading() + 10)
    dusty.left(45)

def turn_right():
    dusty.setheading(dusty.heading() - 10)
    dusty.right(45)

def go_to_click(x, y):
    dusty.goto(x, y)

def reset():
    dusty.home()
    dusty.clear()

# Event listeners for key presses
screen.listen()
screen.onkey(move_forward, "Up")
screen.onkey(move_backward, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")

# Event listener for mouse click
screen.onclick(go_to_click)

# Event listener for reset
screen.onkey(reset, "space")

# Keep the window open
screen.mainloop()