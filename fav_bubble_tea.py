# Bubble Tea Popularity Algorithm
# Author: Donald
# Date: 27 October 2023

# Ask 5 users what their favorite bubble tea place is
# Prints out a summary of the data

# ------ CONSTANTS

NUM_RESPONDENTS = 5

# ------

# Like counters
coco_likes = 0    # Initialize the variable to 0
suntea_likes = 0
chatime_likes = 0
bubqueen_likes = 0

for _ in range(NUM_RESPONDENTS):
    # Ask the user what their favorite place is
    print("What's your favorite bubble tea place?")
    fav_place = input().strip(",.?! ").lower()

    # Tally or counting algo
    if fav_place == "coco":
        coco_likes = coco_likes + 1
    elif fav_place == "suntea":
        suntea_likes += 1
    elif fav_place == "chatime":
        chatime_likes += 1
    elif fav_place == "bubble queen":
        bubqueen_likes += 1

# Percentage counter
coco_percent = int(coco_likes / NUM_RESPONDENTS *100)
suntea_percent = int(suntea_likes / NUM_RESPONDENTS *100)
chatime_percent = int(chatime_likes / NUM_RESPONDENTS *100)
bubqueen_percent = int(bubqueen_likes /NUM_RESPONDENTS *100)

# Print out a summary
# Give the raw score AND the percentage
print(f"Coco Likes: {coco_likes}")
print(f"{coco_percent}% voted for Coco.")
print(f"Suntea Likes: {suntea_likes}")
print(f"{suntea_percent}% voted for Suntea.")
print(f"Chatime Likes: {chatime_likes}")
print(f"{chatime_percent}% voted for Chatime.")
print(f"Bubble Queen likes: {bubqueen_likes}")
print(f"{bubqueen_percent}% voted for Bubble Queen.")