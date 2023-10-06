# Food Suggestion Bot
# Author: Donald
# 6 October 2023

# A bot that asks the user what their favorite food is.
# Based on that food, it will classify the type/genre/cuisine of the food
# It will then give a restaurant suggestion.

import random
import time

# Introduce bot to user
# Ask the user what their favorite food is
print("Hello, I am here to suggest you a restaurant.")
time.sleep(1.2)
fav_food = input("Tell me what your favorite food is. ")
time.sleep(2)

# Italian Cuisine
italian_food = ["pasta", "pizza", "canneloni", "tiramisu"]
# Add another cuisine that our bot should make a suggestion for
japanese_food = ["sushi", "sashimi", "udon", "tempura"]

# If they answer with Italian food, 
# Suggest an Italian restaurant.
# If they answer with Japanese food,
# Suggest a Japanese restaurant.
# If it's neither of the options above,
# Apologise for not being a competent bot.
if fav_food.lower().strip("!.,?") in italian_food:
    print("I see that you might like italian food.")
    time.sleep(2)
    print("I suggest Broli Kitchen.")
    time.sleep(1)
    print("Here's their address:")
    print("186-8180 No 2 Rd, Richmond, BC")
elif fav_food.lower().strip(",.?!") in japanese_food:
    print("I assume that you enjoy japanese cuisine...")
    time.sleep(2)
    print("I suggest the restaurant Ichiro.")
    time.sleep(1)
    print("Here's their address:")
    print("12011 Second Ave #110, Richmond, BC")
else:
    print("Sorry, I don't know what kind of food that is.")
    time.sleep(1.5)
    print("I can't help you, unfortunately.")
    time.sleep(1.5)
    print("I am a very incompetent bot. 😥")