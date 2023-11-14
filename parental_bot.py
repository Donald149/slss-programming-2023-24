# Parental bot
# Author: Donald
# 14 November 2023

# Questions
questions = [
    "Did you eat? ",
    "Did you study? ",
    "Did you do your laundry? ",
    "Did you call grandma? "
]
child_score = 0

for question in questions:
    answer = input(question)
    if answer.lower().strip(" ,.?!") == "yes":
        child_score += 1

if child_score > 2:
    print("Good!")
elif child_score >= 1:
    print("OK...")
else:
    print("I'm coming over.")