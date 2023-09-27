# Chatbot
# Author: Donald
# Date: 20 September 2023

import random
import time

# Greet the user
print("Greetings.")
time.sleep(1.5)
print("I am a chatbot, hoping to learn more about humans.")
time.sleep(2)

# Get the user's name and store it in a variable
user_name = input("To begin with, what's your name? ")

# Respond with the user's name in a friendly way
time.sleep(1.5)
print(f"Great. I look forward to having a great conversation with you, {user_name}.")
time.sleep(2)

# Ask the user what their favourite food is
print("I want to know more about you...")
time.sleep(1)
fav_food = input("What's your favorite food? ")
time.sleep(1)

# If their favorite food is sushi, reply with yum.
if fav_food == "sushi":
    print("Yum! 🍣")
    print("I think I love sushi!")
elif fav_food == "burgers" or fav_food ==  "Burgers":
    print("🍔")
    print("Burgers are great.")
else:
    # Create a list of possible responsees
    list_food_dialogue = [
        f"Oh, I've never had {fav_food} before.",
        f"Sounds delicious, I would like to try {fav_food} one day.",
        "Mmmm. That sounds interesting.",
        f"Umm... you actually like eating {fav_food}?",
        "Cool."
    ]

    # Choose one of those responses randomly
    random_food_dialogue = random.choice(list_food_dialogue)
    # Print out that chosen response
    print(random_food_dialogue)