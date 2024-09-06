import random
import Day11_Blackjack_logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def compare(user_score, computer_score):
    """Comparing scores of both players"""
    if user_score == 21:
        is_game_over = True
        print("You win 😁")
    elif computer_score == 21:
        is_game_over = True
        print("You lose 😤")
    elif user_score == computer_score:
        is_game_over = True
        print("Draw 😵")
    elif computer_score > 21 and user_score > 21:
        is_game_over = True
        print("Draw 😵")
    elif user_score > 21:
        is_game_over = True
        print("Bust. You lose 😭")
    elif computer_score > 21:
        is_game_over = True
        print("Computer bust. You win 😁")
    elif user_score < computer_score:
        is_game_over = True
        print("You lose 😤")
    elif user_score > computer_score:
        is_game_over = True
        print("You win 😁")


def card(user_card_list, user_score, computer_score):
    """Function that helps user draw card"""
    user_deal = False

    while not user_deal:
        user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")

        if user_should_deal == "y":
            user_card_list.append(random.choice(cards))
            user_score = sum(user_card_list)
            print(f"Your current cards: {user_card_list}, current score: {user_score}")

            if user_score > 21 and 11 in user_card_list:
                user_card_list.remove(11)
                user_card_list.append(1)
                user_score = sum(user_card_list)
                print(f"Your cards: {user_card_list}, current score: {user_score}")
            if user_score > 21 and 11 not in user_card_list:
                break
        elif user_should_deal == "n":
            user_deal = True
        else:
            print("Invalid input. Please type 'y' or 'n'.")

    compare(user_score, computer_score)


def blackjack_game():
    """start of card game"""
    for lines in Day11_Blackjack_logo.logo:
        print(lines)
    is_game_over = False
    user_cards = []
    computer_cards = []

    for _ in range(2):
        user_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))

    while not is_game_over:
        user_score = sum(user_cards)
        computer_score = sum(computer_cards)
        while computer_score < 17:
            computer_cards.append(random.choice(cards))
            computer_score = sum(computer_cards)
            if sum(computer_cards) > 21 and 11 in computer_cards:
                computer_cards.remove(11)
                computer_cards.append(1)
            computer_score = sum(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")

        print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
        print(f"Computer's first card: {computer_cards[0]}")

        card(user_cards, user_score, computer_score)

        print(f"Your final hand: {user_cards}, final score: {sum(user_cards)}")
        print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")

        again = input("Do you want to play again? Type 'y' or 'n': ")
        if again == 'y':
            print("\n"*100)
            blackjack_game()
        else:
            print("Thanks for playing!")
            break

blackjack_game()
