# World Traveller
# Author: Donald
# 1 November 2023

# Greetings
print("Hello! What's your name?")
user_name = input().strip(",.?! ")
print(f"It's nice to meet you, {user_name}!")

# Continent counter
continent_list = ["Asia", "Europe", "North America", "South America", "Australia", "Africa", "Antarctica"]
traveller_score = 0

for continent in continent_list:
    print(f"Have you been to {continent}?")
    yes_no = input().strip(",.?!").lower()
    if yes_no == "yes":
        traveller_score += 1

print(f"I see, you've visited {traveller_score}/7 continents!")