# Pumpkin Drawing
# Author: Donald
# Date: 31 October 2023

import turtle
import time

window = turtle.Screen()
window.bgcolor("black")

# Stem
stem = turtle.Turtle()
stem.hideturtle()
stem.color("green")
stem.penup()
stem.setposition(0, 200)
stem.pensize(30)
stem.pendown()
stem.setposition(0, 225)

# Whole pumpkin
pumpkin = turtle.Turtle()
pumpkin.hideturtle()
pumpkin.color("orange")
pumpkin.setposition(-50, 100)
pumpkin.dot(200)
pumpkin.pensize(200)
pumpkin.setposition(50, 100)

# The turtle to "carve" the pumpkin
carver = turtle.Turtle()

# "Flatten" the lower part of the pumpkin
carver.penup()
carver.hideturtle()
carver.setposition(-200, -15)
carver.pensize(60)
carver.pendown()
carver.forward(600)
carver.pensize(2)

# Body
bigpumpkin = turtle.Turtle()
bigpumpkin.hideturtle()
bigpumpkin.penup()
bigpumpkin.color("Orange")
bigpumpkin.setposition(0, -150)
bigpumpkin.dot(400)

# Eye
carver.penup()
carver.setposition(-60, 130)
carver.dot(75)
carver.penup()
carver.forward(120)
carver.dot(75)

# Mouth
carver.penup()
carver.setposition(-50, 60)
carver.pensize(5)
carver.pendown()
carver.forward(100)
carver.penup()

# Buttons
carver.setposition(0,-30)
carver.dot(40)
carver.setposition(0,-100)
carver.dot(60)

# Hands
hands = turtle.Turtle()
hands.hideturtle()
hands.penup()
hands.color('#532915')
hands.setposition(180, -60)
hands.dot(30)
hands.pendown()
hands.pensize(30)
hands.setposition(260,20)
hands.penup()
hands.setposition(-180, -60)
hands.pendown()
hands.setposition(-260, 20)

turtle.done()