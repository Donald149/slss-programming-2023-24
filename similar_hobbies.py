# Similar hobbies
# Author: Donald
# 14 November 2023

# Ask for imput
print("Please enter what hobbies you enjoy, seperated by spaces.")
person1 = input("Person 1:   ").lower().split(" ")
person2 = input("Person 2:   ").lower().split(" ")

# Initialize values
sim_score = 0

# Algo
for hobby in person1:
    if hobby in person2:
        sim_score += 1

# Results
print(f"You have {sim_score} hobbies in common!")