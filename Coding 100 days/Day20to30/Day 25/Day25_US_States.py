import pandas as pd
import turtle

# Read the data from the CSV file
data = pd.read_csv("50_states.csv")

# Create a dictionary from the data
state_data = {
    "State": data["state"],
    "x": data["x"],
    "y": data["y"]
}

# Create a DataFrame from the dictionary
df = pd.DataFrame(state_data)

# Create a turtle object
screen = turtle.Screen()
screen.title("US States")
screen.setup(width=800, height=600)

# Load the image of the US map
image = "Day25_US_Map.gif"
screen.addshape(image)
turtle.shape(image)

# Create a turtle object
t = turtle.Turtle()
t.penup()
t.hideturtle()

# Display the state name at the x, y coordinates
for index, row in df.iterrows():
    t.goto(row["x"], row["y"])
    t.write(row["State"], align="center", font=("Arial", 8, "normal"))

screen.mainloop()





