# Turtle Example
# Author: DOnald
# 21 November 2023

import turtle

# Create a turtle that can be moved around the screen

FORWARD_MAGNITUDE = 20
TURN_ANGLE = 90

# Make a turtle object
paint = turtle.Turtle()

# Get some input from the user
print("""To give commands, type:
W - to go forward
A - to turn left
D - to turn right.""")

# Repeat the below forever or the user says stop
done = False

while not done :
    command = input("Where shall I move torwards to? ").strip(",.?! ").lower()

    # Move the turtle around based on that input
    if command in ["w", "forward"]:
        paint.forward(FORWARD_MAGNITUDE)
    elif command in ["a", "left"]:
        paint.left(TURN_ANGLE)
    elif command in ["d", "right"]:
        paint.right(TURN_ANGLE)
    elif command == "stop":
        done = True