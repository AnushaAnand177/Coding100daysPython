print("Lets play Rock, Paper, Scissors".capitalize())

import random

options = ["Rock", "Paper", "Scissors"]

computer = random.choice(options)

player = None
#This line initializes the player variable to None,
# indicating that the player's choice has not been made yet

while player not in options:
    player = input("Rock, Paper or Scissors? ").capitalize()

if player == computer:
    print("Tie!")
elif player == "Rock":
    if computer == "Paper":
        print("Computer Wins!")
    else:
        print("Player Wins!")
elif player == "Paper":
    if computer == "Scissors":
        print("Computer Wins!")
    else:
        print("Player Wins!")
elif player == "Scissors":
    if computer == "Rock":
        print("Computer Wins!")
    else:
        print("Player Wins!")
else:
    print("Invalid Input!")