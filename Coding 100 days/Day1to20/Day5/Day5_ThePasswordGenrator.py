import random

alphabets = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
Alphabets = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
letters_list = alphabets + Alphabets
digits = ["0","1","2","3","4","5","6","7","8","9"]
symbols = ["!","#","$","%","&","*","(",")","-",".","/",":",";","<","=",">","?","@","~"]

print("Welcome to the PyPassword Generator!")

pr_letters= int(input("How many letters would you like in your password?\n"))
pr_symbols = int(input(f"How many symbols would you like?\n"))
pr_numbers = int(input(f"How many numbers would you like?\n"))

password = []


"""In Python, the `+=` operator is overloaded for strings, which means it can be used for concatenation 
(joining strings together) instead of just addition.

When you use `password += random.choice(letters_list)`, Python is essentially doing 
`password = password + random.choice(letters_list)`. 
This is concatenating the existing string `password` with the new character selected from `letters_list`.

So, even though `random.choice(letters_list)` returns a string (a single character), 
the `+=` operator is used to concatenate it to the end of the existing string `password`, 
rather than trying to perform arithmetic addition."""

for char in range(0,pr_letters):
    password += random.choice(letters_list)
for char in range(0,pr_symbols):
    password += random.choice(symbols)
for char in range(0,pr_numbers):
    password += random.choice(digits)

random.shuffle(password)

password = "".join(password)
'''The .join(password) operation concatenates all the strings in the list password together into one string,
with no separator between them.'''


print(password)