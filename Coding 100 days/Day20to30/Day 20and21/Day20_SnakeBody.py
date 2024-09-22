from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        """
        Initializes a new instance of the class, setting up the initial state.

        Attributes:
            segments (list): A list to store the segments of the snake.
            head (Any): The first segment of the snake, representing the head.
        """
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]



    def create_snake(self):
        """
        Creates the initial snake by adding segments based on starting positions.

        :return: None
        """
        starting_positions = [(0, 0), (-20, 0), (-40, 0)]
        for position in starting_positions:
            self.add_segment(position)

    def add_segment(self, position):
        """
        :param position: A tuple representing the (x, y) coordinates where the new segment will be added.
        :return: None
        """
        new_segment = Turtle("square")
        new_segment.color("white", "white")
        new_segment.turtlesize(1, 1)
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def move(self):
        """
        Moves the segments of the object such that each segment follows the position of the segment in front of it, with the head segment moving forward by a predefined distance.

        :return: None
        """
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def direction_up(self):
        """
        Updates the direction of the head to upwards if the current heading is not downwards.

        :return: None
        """
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def direction_down(self):
        """
        Changes the direction of the snake's head to down if the current direction is not up.

        :return: None
        """
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def direction_left(self):
        """
        Sets the heading direction of the snake to the left if it is not currently heading right.

        :return: None
        """
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def direction_right(self):
        """
        Sets the direction of the snake's head to the right if it is not currently heading left.

        :return: None
        """
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def snake_extend(self):
        """
        Extends the length of the snake by adding a new segment at the position of the last segment.

        :return: None
        """
        self.add_segment(self.segments[-1].position())







