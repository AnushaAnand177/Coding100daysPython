print("Welcome to Love Calculator")

def calclulate_love_score(first_name, second_name):

    first_name = first_name.lower()
    second_name = second_name.lower()

    true_count = 0
    love_count = 0

    for letter in first_name:
        if letter in "true":
            true_count += 1

    for letter in second_name:
        if letter in "love":
            love_count += 1

    love_score = str(true_count) + str(love_count)

    return int(love_score)