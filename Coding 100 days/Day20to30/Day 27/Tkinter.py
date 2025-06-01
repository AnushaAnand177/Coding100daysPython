import tkinter as tk
from tkinter import Entry
from tkinter.ttk import Button

def calculate():
    # Get the value from miles_entry, convert to float
    try:
        miles_value = float(miles_entry.get())
        # Convert to kilometers (1 mile = 1.60934 km)
        km_value = miles_value * 1.60934
        # Update the kilometer_result label
        kilometer_result.config(text=f"{km_value:.2f}")
    except ValueError:
        kilometer_result.config(text="Invalid input")

# Create the main window
window = tk.Tk()

# Set the window title
window.title("My Window")
# Set window size (width x height)
window.geometry("400x300")

miles_entry = Entry()
miles_entry.grid(column=1, row=0)

miles = tk.Label(window, text="miles")
miles.grid(column=2, row=0)

is_equal_to = tk.Label(window, text="is equal to")
is_equal_to.grid(column=0, row=1)

kilometer_result = tk.Label(window, text="0")
kilometer_result.grid(column=1, row=1)

kms = tk.Label(window, text="kms")
kms.grid(column=2, row=1)

# Add the command parameter to link the button with the calculate function
calc_btn = Button(text="Calculate", command=calculate)
calc_btn.grid(column=1, row=2)

# Start the main event loop
window.mainloop()