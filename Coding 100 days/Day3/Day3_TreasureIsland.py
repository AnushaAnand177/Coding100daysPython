print("WELCOME TO TREASURE ISLAND")
print("Your mission is to find the treasure.")

choice1 = input("You're at a cross road. Where do you want to go? Type 'left' or 'right' ")
choice2 = input("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across. ")
choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ")

if choice1 == "left":
    if choice2 == "wait":
        if choice3 == "yellow":
            print("YOU FOUND THE TREASURE!!")
        else:
            print("YOU'RE DEAD!!")
    else:
        print("YOU'RE DEAD!!")
else:
    print("YOU'RE DEAD!!")