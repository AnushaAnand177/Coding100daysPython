# Tkinter GUI Development Guide
## 1. Creating a Window
``` python
import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("My Application")
window.geometry("400x300")  # Width x Height

# Start the main event loop
window.mainloop()
```
## 2. Using Grid Layout
``` python
# Grid layout example
label = tk.Label(window, text="Name:")
entry = tk.Entry(window)

label.grid(row=0, column=0, padx=5, pady=5)
entry.grid(row=0, column=1, padx=5, pady=5)
```
## 3. Creating Buttons
``` python
def button_click():
    print("Button clicked!")

# Create a button
button = tk.Button(
    window,
    text="Click Me",
    command=button_click,
    bg="blue",        # background color
    fg="white",       # text color
    width=10,
    height=2
)
button.grid(row=1, column=0, pady=10)
```
## 4. Creating Labels
``` python
# Simple text label
text_label = tk.Label(
    window,
    text="Hello World",
    font=("Arial", 14),
    fg="black"
)
text_label.grid(row=0, column=0)

# Label with background color
colored_label = tk.Label(
    window,
    text="Colored Label",
    bg="yellow",
    padding=10
)
colored_label.grid(row=1, column=0)
```
## 5. Adding Images
``` python
from PIL import Image, ImageTk

# Load and resize image
image = Image.open("image.png")
image = image.resize((100, 100))  # Resize to 100x100 pixels
photo = ImageTk.PhotoImage(image)

# Create label with image
image_label = tk.Label(
    window,
    image=photo
)
image_label.image = photo  # Keep a reference!
image_label.grid(row=0, column=0)
```
## Complete Example
``` python
import tkinter as tk
from PIL import Image, ImageTk

def create_gui():
    # Create main window
    window = tk.Tk()
    window.title("Sample Application")
    window.geometry("500x400")
    
    # Create and place widgets
    title_label = tk.Label(
        window, 
        text="Welcome!", 
        font=("Arial", 16)
    )
    title_label.grid(row=0, column=0, columnspan=2, pady=20)
    
    # Entry with label
    name_label = tk.Label(window, text="Enter name:")
    name_label.grid(row=1, column=0, padx=5, pady=5)
    
    name_entry = tk.Entry(window)
    name_entry.grid(row=1, column=1, padx=5, pady=5)
    
    # Button
    submit_button = tk.Button(
        window,
        text="Submit",
        command=lambda: print(f"Hello, {name_entry.get()}")
    )
    submit_button.grid(row=2, column=0, columnspan=2, pady=10)
    
    window.mainloop()

if __name__ == "__main__":
    create_gui()
```
## Important Tips:
1. **Grid Layout**:
    - Use `padx` and `pady` for padding
    - to span multiple columns `columnspan`
    - for alignment (N, S, E, W) `sticky`

2. **Images**:
    - Always keep a reference to `PhotoImage`
    - Use PIL for more image format support
    - Common formats: PNG, GIF

3. **Widgets**:
    - Most widgets share common options like `bg`, `fg`, `font`
    - Use `command` for button click events
    - Use `textvariable` with `StringVar()` for dynamic text

4. **Window Properties**:
    - `resizable(width, height)` to control resizing
    - `iconbitmap()` to set window icon
    - `configure(bg="color")` to set window background

To use this code, make sure you have the required packages installed:
``` bash
pip install pillow
```
This guide covers the basics of Tkinter GUI development. Each element can be further customized with additional parameters and styling options.
