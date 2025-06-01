import time
from turtle import Screen
from Day22_Pong_Paddle import Paddle
from Day22_Pong_Ball import Ball
from Day22_Pong_Scoreboard import Scoreboard

# Set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# Create ball, paddles, and scoreboard
ball = Ball()
paddle_right = Paddle((250, 0))
paddle_left = Paddle((-250, 0))
scoreboard = Scoreboard()

# Define paddle controls
screen.listen()
screen.onkey(paddle_right.go_up, "Up")
screen.onkey(paddle_right.go_down, "Down")
screen.onkey(paddle_left.go_up, "w")
screen.onkey(paddle_left.go_down, "s")

# Game loop
game_is_on = True
while game_is_on:
    time.sleep(0.07)  # Reduced sleep time for more responsive gameplay
    screen.update()
    ball.move()

    # Handle ball collision with paddles
    ball.handle_paddle_hit(paddle_left)
    ball.handle_paddle_hit(paddle_right)

    # Handle ball collision with walls
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    # Handle ball going out of bounds
    if ball.xcor() > 290:
        ball.reset()
        ball.bounce_x()
        scoreboard.left_point()
    elif ball.xcor() < -290:
        ball.reset()
        ball.bounce_x()
        scoreboard.right_point()

    # Ensure paddles do not move outside the screen area
    if paddle_right.ycor() > 250:
        paddle_right.goto(paddle_right.xcor(), 250)
    elif paddle_right.ycor() < -250:
        paddle_right.goto(paddle_right.xcor(), -250)

    if paddle_left.ycor() > 250:
        paddle_left.goto(paddle_left.xcor(), 250)
    elif paddle_left.ycor() < -250:
        paddle_left.goto(paddle_left.xcor(), -250)

    # Check for game over condition
    if scoreboard.left_score >= 10 or scoreboard.right_score >= 10:
        game_is_on = False

screen.mainloop()