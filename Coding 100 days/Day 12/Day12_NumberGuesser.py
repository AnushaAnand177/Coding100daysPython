import random

print("Welcome to number guesser game")

def random_number():
    """
    Generates a random number between 1 and 100.

    Returns:
        int: The randomly generated number.
    """
    random_number = random.randint(1,100)
    return random_number

def difficulty_level():
    """
    Asks the user to choose a difficulty level and returns the corresponding number of lives.

    Returns:
        int: The number of lives for the chosen difficulty level.
    """
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return 10
    elif level == "hard":
        return 5
    else:
        print("Wrong input. Try again")
        difficulty_level()


def life(lives):
    """
       Returns the number of lives for the current game.

       Args:
           lives (int): The number of lives for the current game.

       Returns:
           int: The number of lives for the current game.
       """
    playing = True
    while playing:
        if lives != 0:
            return lives

def guess(random_number, lives):
    """
        Plays the number guessing game.

        Args:
            random_number (int): The randomly generated number to guess.
            lives (int): The number of lives for the current game.

        Returns:
            None
        """
    no_of_lives = life(lives)
    print(f"You have {no_of_lives} lives left")
    print("Guess a number between 1 and 100")
    while guess != random_number and no_of_lives != 0:
        user_guess = int(input("Make a guess: "))
        if user_guess == random_number:
            print("You guessed right")
            break
        elif user_guess > random_number:
            print("You guessed too high")
            no_of_lives -= 1
            print(f"You have {no_of_lives} lives left")
        elif user_guess < random_number:
            print("You guessed too low")
            no_of_lives -= 1
            print(f"You have {no_of_lives} lives left")
    if no_of_lives == 0:
        print("You lost all your lives. Game over")
    print(f"The number was {random_number}")
guess(random_number(), difficulty_level())