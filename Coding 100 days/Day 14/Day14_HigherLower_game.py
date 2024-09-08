from Day14_HigerLower_Art import logo, vs
import random
import Day14_HigherLower_data

print(logo)

'''-------------------SELECTING DATA--------------------------'''
def selecting():
    data = random.choice(Day14_HigherLower_data.data)
    for key, value in data.items():
        return data["name"], data["description"], data["country"], data["follower_count"]


'''------------------------INPUT FROM USER----------------------------'''
def input_from_user():
    return input("Who has more followers? Type 'A' or 'B': ")


'''------------------------MAIN GAME-----------------------------------'''
def game():
    playing = True
    name, description, country, follower_count = selecting()
    name2, description2, country2 , follower_count2 = selecting()
    score = 0
    while playing:
        print(f"You're Current score: {score}.")
        print(f"Compare A: {name}, a {description}, from {country}")
        print(vs)
        print(f"Against B: {name2}, a {description2}, from {country2}")

        choice = input_from_user()
        if choice == "A":
            if follower_count > follower_count2:
                score += 1
                name, description, country, follower_count = name2, description2, country2, follower_count2
                name2, description2, country2, follower_count2 = selecting()
                print("You are right!\n")
            else:
                print("Sorry, that's wrong.\n")
                playing = False
        elif choice == "B":
            if follower_count2 > follower_count:
                score += 1
                name, description, country, follower_count = name2, description2, country2, follower_count2
                name2, description2, country2, follower_count2 = selecting()
                print("You are right!\n")
            else:
                print("Sorry, that's wrong.\n")
                playing = False
        else:
            print("Invalid input. Please enter 'A' or 'B'.\n")





game()

