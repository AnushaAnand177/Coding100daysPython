# 100 Days of Code - Angela Yu

# change the name of the names and replace it with the name of the person you want to send the letter to
with open("../Day 24/Input/names/invited names.txt", "r") as file:
    names = file.readlines()
    for name in names:
        with open("../Day 24/Input/letters/letter.txt", "r") as letter:
            letter_content = letter.read()
            new_letter = letter_content.replace("[name]", name.strip())
            with open(f"../Day 24/Output/ready to Send/letter_for_{name.strip()}.txt", "a") as new_file:
                new_file.write(new_letter)

