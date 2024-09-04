
import Day7_HangmanLogo
import Day7_Hangman_Art
import Day7_Hangman_Words
import random


logo = Day7_HangmanLogo.logo
print("Welcome to the hangman game".capitalize())


word = Day7_Hangman_Words.words
hangman = Day7_Hangman_Art.HANGMANPICS
word = random.choice(word)

attempts = 6
num = 0
blank = ["_"] * len(word)
while "_" in blank:
        display = "".join(blank)
        guess = input(f"Guess a letter: {display}\n")
        for i in range(len(word)):
            if guess == word[i]:
                blank[i] = guess
                if blank == word:
                    print(f"You win. The word was {word}")
                    break
        if guess not in word:
            print(hangman[num])
            num += 1
            attempts -= 1
            print(f"You have {attempts} attempts left")
            if num == 6:
                print(f"You lose. The word was {word}")
                break


