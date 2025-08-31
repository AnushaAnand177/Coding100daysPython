import tkinter as tk
import random
from tkinter import messagebox

def pswd():
    symb = "!@#$%^&*()?"
    alphabets = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'

    # Get values at button click
    char = option.get()
    no_of_char = length.get()

    if char == "symbols":
        chars = symb
    elif char == "alphabets":
        chars = alphabets
    elif char == "numbers":
        chars = numbers
    else:
        chars = symb + alphabets + numbers

    # Generate password (choices allows repetition)
    password = "".join(random.choices(chars, k=no_of_char))

    # Show password in messagebox

    with open("password.txt", "a") as file:
        file.write(f"{entry_user.get()} ||  {entry_website.get()} || {password}\n")

root = tk.Tk()
root.title("Password Generator")
root.geometry("500x200")

# Username + Website
tk.Label(root, text="Username").grid(row=0, column=0, padx=10, pady=5)
tk.Label(root, text="Website Name").grid(row=1, column=0, padx=10, pady=5)

entry_user = tk.Entry(root)
entry_website = tk.Entry(root)
entry_user.grid(row=0, column=1)
entry_website.grid(row=1, column=1)

# Character type options
tk.Label(root, text="Contains:").grid(row=2, column=0, padx=10, pady=5)
option = tk.StringVar(value="symbols")  # default value
tk.Radiobutton(root, text="Symbols", variable=option, value="symbols").grid(row=2, column=1)
tk.Radiobutton(root, text="Alphabets", variable=option, value="alphabets").grid(row=2, column=2)
tk.Radiobutton(root, text="Numbers", variable=option, value="numbers").grid(row=2, column=3)

# Password length options
tk.Label(root, text="Length:").grid(row=3, column=0, padx=10, pady=5)
length = tk.IntVar(value=6)  # default value
tk.Radiobutton(root, text="6", variable=length, value=6).grid(row=3, column=1)
tk.Radiobutton(root, text="12", variable=length, value=12).grid(row=3, column=2)
tk.Radiobutton(root, text="18", variable=length, value=18).grid(row=3, column=3)

# Generate Button
tk.Button(root, text="Generate Password", command=pswd).grid(row=4, column=1, columnspan=2, pady=10)

root.mainloop()


# print(help(tk.Radiobutton))