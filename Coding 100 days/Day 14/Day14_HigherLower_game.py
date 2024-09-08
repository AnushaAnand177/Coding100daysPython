import random
from Day14_HigherLower_data import data
from Day14_HigerLower_Art import logo, vs

# Printing the logo as before
print(logo)

'''-------------------SELECTING DATA--------------------------'''


# Created a concise function to select a person's data
# This returns a dictionary with all necessary information in one go
def select_data():
    person = random.choice(data)
    return {
        "name": person["name"],
        "description": person["description"],
        "country": person["country"],
        "followers": person["follower_count"]
    }


'''------------------------INPUT FROM USER----------------------------'''


# Changed the name to `get_user_choice` for clarity
# This function ensures user input is processed uniformly by using `.strip().upper()`
def get_user_choice():
    return input("Who has more followers? Type 'A' or 'B': ").strip().upper()


'''------------------------CHECK WINNER-----------------------------'''


# Created a separate function to handle the comparison logic.
# It simplifies the main game loop and avoids redundant code for checking 'A' or 'B'
def is_correct_choice(choice, a_followers, b_followers):
    if choice == "A":
        return a_followers > b_followers
    elif choice == "B":
        return b_followers > a_followers
    return False  # Added a fallback if input is invalid, though it will be handled later


'''------------------------MAIN GAME-----------------------------------'''


def game():
    score = 0
    playing = True

    # Now only two selections at the start: person_a and person_b
    # Eliminated the need for separate variables for name, description, etc.
    person_a = select_data()
    person_b = select_data()

    while playing:
        # Displaying the current score and the details of person A and B
        print(f"You're current score: {score}.")
        print(
            f"Compare A: {person_a['name']}, a {person_a['description']}, from {person_a['country']}")
        print(vs)
        print(
            f"Against B: {person_b['name']}, a {person_b['description']}, from {person_b['country']}")

        choice = get_user_choice()

        # Using the helper function to check if the choice was correct
        if is_correct_choice(choice, person_a['followers'], person_b['followers']):
            score += 1
            print("You are right!\n")

            # Instead of reassigning all variables manually, person_a becomes person_b
            # This reduces redundancy and improves code clarity
            person_a = person_b
            person_b = select_data()  # Then we select a new person_b
        else:
            print(f"Sorry, that's wrong. Final score: {score}.\n")
            playing = False  # End the game if the guess is incorrect


# Start the game
game()
