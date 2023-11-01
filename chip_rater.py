# Chip Rater
# Author: Donald
# 1 November 2023

# Interview people abot their
# perception of how delicious chips are
# based on a set of questions
# In the end, we'll give an average score.

# Greet the user
print("Please answer the following questions based on the chip you just ate.")

# Create a list of questions to ask
questions = [
    "How crispy was the chip on a scale from 1 to 5?"
    " 5 is very crispy. 1 is mushy.",
    "How would you rate the taste from 1 to 5?"
    " 5 is the best. 1 is worse than dirt.",
    "From 1 to 5, how would you rate the packaging?"
    " 5 is would buy just for packaging. 1 is just some rotten wet paper bag."
]

final_score = 0

# Ask the questions to the user
for question in questions:
    print(question)

    # Store their response
    rating = int(input().strip(",.?! "))
    final_score += rating

# Do some math - average
average_score = final_score / len(questions)

# Present the results to the user
print(f"The average score for this chip is: {average_score:.1f}/5")