import time
import turtle
from turtle import Screen, Turtle
from Day20_SnakeBody import Snake
from Day21_Snake_Food import Food
from Day21_Snake_ScoreBoard import ScoreBoard


# Setup screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

tim = Snake()
food = Food()
score = ScoreBoard()
screen.listen()
screen.onkey(tim.direction_up, "Up")
screen.onkey(tim.direction_down, "Down")
screen.onkey(tim.direction_left, "Left")
screen.onkey(tim.direction_right, "Right")

game_is_on = True
try:
    while game_is_on:
        screen.update()
        time.sleep(0.2)
        tim.move()

        # Check for collision with the screen boundary
        if (tim.head.xcor() > 295 or tim.head.xcor() < -295 or tim.head.ycor() > 295
                or tim.head.ycor() < -295):
            score.game_over()
            game_is_on = False  # Stop the game when the snake hits a boundary

        for index in tim.segments:
            if index == tim.head:
                pass
            elif tim.head.distance(index) < 10:
                score.game_over()
                game_is_on = False

        # Check for collision with the food
        if tim.head.distance(food) < 15:
            food.food_position()
            tim.snake_extend()
            score.increase_score()

except turtle.Terminator:
    print("Game terminated unexpectedly.")

screen.exitonclick()  # Close the window on click
