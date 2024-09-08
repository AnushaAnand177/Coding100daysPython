import random
from Day14_HigherLower_data import data
from Day14_HigerLower_Art import logo, vs

print(logo)

'''-------------------SELECTING DATA--------------------------'''


def select_data():
    person = random.choice(data)
    return {
        "name": person["name"],
        "description": person["description"],
        "country": person["country"],
        "followers": person["follower_count"]
    }


'''------------------------INPUT FROM USER----------------------------'''


def get_user_choice():
    return input("Who has more followers? Type 'A' or 'B': ").strip().upper()


'''------------------------CHECK WINNER-----------------------------'''


def is_correct_choice(choice, a_followers, b_followers):
    if choice == "A":
        return a_followers > b_followers
    elif choice == "B":
        return b_followers > a_followers
    return False


'''------------------------MAIN GAME-----------------------------------'''


def game():
    score = 0
    playing = True

    person_a = select_data()
    person_b = select_data()

    while playing:
        print(f"You're current score: {score}.")
        print(
            f"Compare A: {person_a['name']}, a {person_a['description']}, from {person_a['country']}")
        print(vs)
        print(
            f"Against B: {person_b['name']}, a {person_b['description']}, from {person_b['country']}")

        choice = get_user_choice()
        if is_correct_choice(choice, person_a['followers'], person_b['followers']):
            score += 1
            print("You are right!\n")
            # Make 'B' the new 'A' and select a new 'B'
            person_a = person_b
            person_b = select_data()
        else:
            print(f"Sorry, that's wrong. Final score: {score}.\n")
            playing = False


# Start the game
game()


