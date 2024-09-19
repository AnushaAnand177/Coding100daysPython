from turtle import Turtle, Screen
import random

# Set up screen
screen = Screen()
screen.setup(width=1000, height=550)
screen.title("Turtle Race")

# Create turtles
colors = ["red", "blue", "green", "yellow", "purple", "orange", "brown", "pink", "black",
          "violet"]
turtles = []
start_y = -215  # Starting y-position for the first turtle

# Initialize each turtle, set color and position
for color in colors:
    turtle = Turtle(shape="turtle")
    turtle.color(color)
    turtle.penup()
    turtle.goto(x=-400, y=start_y)  # Starting point for each turtle
    turtles.append(turtle)
    start_y += 50  # Adjust y-position for the next turtle

# Set the finish line at x = 400
finish_line_x = 400

# Draw the finish line
finish_line = Turtle()
finish_line.color("black")
finish_line.penup()
finish_line.goto(x=finish_line_x, y=-240)
finish_line.pendown()
finish_line.width(3)
finish_line.setheading(90)
finish_line.forward(490)
finish_line.hideturtle()

# Ask for the number of players
num_players = int(
    screen.numinput("Number of Players", "How many players are betting?", minval=1,
                    maxval=10))

# Setup to ask for players' names and their bets on which turtle will win
players = []
bets = []

for i in range(num_players):
    name = screen.textinput(f"Player {i + 1}", "What is your name? ")
    bet = screen.textinput(f"{name}'s Bet", "Which turtle color do you bet on? ")

    # Ensure the bet is a valid turtle color
    while bet.lower() not in colors:
        bet = screen.textinput(f"{name}'s Bet",
                               f"Invalid color! Please choose from {', '.join(colors)}: ")

    players.append(name)
    bets.append(bet.lower())

# Run the race
winner = None
while winner is None:
    for turtle in turtles:
        # Move each turtle forward a random distance
        turtle.forward(random.randint(1, 10))

        # Check if any turtle has crossed the finish line
        if turtle.xcor() >= finish_line_x:
            winner = turtle
            break

# Announce the winner for the race
winner_color = winner.pencolor()
print("Race Over!", f"The {winner_color} turtle has won the race!")

# Determine if any player's bet was correct
winners = []
for i in range(num_players):
    if bets[i] == winner_color:
        winners.append(players[i])

if winners:
    print(f"Congratulations to {', '.join(winners)}! You guessed correctly!")
else:
    print("No one guessed correctly this time.")

screen.exitonclick()
