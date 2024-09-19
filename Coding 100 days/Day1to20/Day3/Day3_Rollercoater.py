print("Welcome to Ride on Sundays\n Enter your height to check if you are eligible to ride the Rollercoaster")

height = int(input("What is your height in cm? "))
age = int(input("What is your age? "))
photo = input("Do you want a photo taken? ")
bill = 0
if height >= 120:
    print("You can ride the Rollercoaster")
    if age < 12:
        bill = 5
    elif age >12 and age <= 18:
        bill = 7
    elif age > 18:
        bill = 12
    elif age >= 45 and age <= 55:
        bill = 0
else:
    print("Sorry, you have to grow taller before you can ride")

if photo == "yes":
    bill += 3
else:
    print("Thank you")

print("Thank you, Your bill is: " + str(bill))