# SFU's Best
# Author: Donald
# 10 November 2023

# Load data from .csv file
# Read it in a meaningful way
# Link similarities score algo to the data

# Open the file
with open("./data.csv") as f:
    # Read the first line of data
    
    f.readline()
    
# Create a "profile" for someone that shows their favorite places at sfu
profile = [
    "Bubble World",
    "Chef Hung",
    "Pizza Hut",
    "Guadalupe (MBC)",
    "Subway"
]

# Initialize our top similarity score and their name
top_sim_score = 0
top_sim_name = ""

# Initialize least similarity score
lowest_score = 0
lowest_name = ""

with open("./data.csv") as f:
    # Throw away the header line
    header = f.readline()

    #  For every line of data in the file (string)
    for line in f:
        # convert the line of data into a list
        current_likes = line.split(",")

        # initialize the current score
        # store the current person's name
        current_sim_score = 0
        current_name = current_likes[1]

        # sim score algo
        for item in profile:
            if item in current_likes:
                current_sim_score += 1

        # print the current sim score
        print(f"{current_name}- Score: {current_sim_score}")

        # Update the top score if this is highest
        if current_sim_score > top_sim_score:
            # update the top score
            top_sim_score = current_sim_score
            top_sim_name = current_name

        # Update the lowest score if its lower
        if current_sim_score <= lowest_score:
            # update the lowest score
            lowest_score = current_sim_score
            lowest_name = current_name

print("TOP SIMILAR PERSON!")
print(f"{top_sim_name} - Score: {top_sim_score}")

print("Least similar person:")
print(f"{lowest_name} - {lowest_score}")