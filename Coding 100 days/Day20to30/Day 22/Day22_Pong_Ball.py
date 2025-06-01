from turtle import Turtle

# Ball.py
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9  # Increase speed

    def reset(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()

    def handle_paddle_hit(self, paddle):
        if self.distance(paddle) < 50 and (self.xcor() > 320 or self.xcor() < -320):
            self.bounce_x()

'''
condition: ball will bounce when it touches the walls either upper wall or lower wall
how: lower and right : ycor + 10 and xcor + 10 or 
     upper and left : ycor - 10 and xcor - 10 or 
     upper and right :ycor - 10 and xcor + 10 or 
     lower and left: ycor + 10 and xcor - 10 
'''




