# Chatbot
# Author: Donald
# Date: 20 September 2023

# Greet the user
print("Greetings.")
print("I am a chatbot, hoping to learn more about humans.")

# Get the user's name and store it in a variable
user_name = input("To begin with, what's your name? ")

# Respond with the user's name in a friendly way
print(f"Great. I look forward to having a great conversation with you, {user_name}.")

# Ask the user what their favourite food is
fav_food = input("Let's see... what food do you like the most? ")

# Make a comment about their food but have multiple dialogue options
# Create a list of possible responsees
list_food_dialogue = [
    f"Oh, I've never had {fav_food} before.",
    f"Sounds delicious, I would like to try {fav_food} one day.",
    "Mmmm. That sounds interesting.",
    f"Umm... you actually like eating {fav_food}?",
    "Cool."
]

# Choose one of those responses randomly
import random
random_food_dialogue = random.choice(list_food_dialogue)

# Print out that chosen response
print(random_food_dialogue)