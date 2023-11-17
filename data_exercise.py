# Data Exercise
# Author: Donald
# 15 November 2023

"""Instructions:

Put this file in your programming folder.
Download the data-example.csv file and put it in this same folder.
For each problem, design a solution.
Each part builds on the previous step, so don't skip any.
You can refer to the work that we did last day for any hints.
Do not use any generative AI for the solutions."""

# Since our file has some symbols in it, this is the most effective way at opening up the file.

with open("./data_example.csv", encoding="utf-8") as f:
    f.readline()

# Note that I've set the encoding parameter to "utf-8"

# --- Problems

# Problem 1:
# Open the file and print the contents of the second line in the file.

with open("./data_example.csv", encoding="utf-8") as f:
    header = f.readline()
    print(f.readline())

# Problem 2:
# Good! Now that you've done that, open the file, and print out every line of data.

with open("./data_example.csv", encoding="utf-8") as f:
    header = f.readline()
    for line in f:
        print(f.readline().strip())

# Problem 3:
# If you've made it this far, well done. Next task:
# Convert that line of data into a list.

with open("./data_example.csv", encoding="utf-8") as f:
    header = f.readline()
    for line in f:
        current_data = line.strip().split(",")

# Problem 4:
# Give yourself a pat on the back.
# See if you can count how many people like "Chicken Adobo" as their favourite food.

chicken_likes = 0

with open("./data_example.csv", encoding="utf-8") as f:
    header = f.readline()
    for line in f:
        current_data = line.strip().split(",")

        if "Chicken Adobo" in current_data:
            chicken_likes += 1

print(f"There are {chicken_likes} people who like Chicken Adobo.")

# Problem 5:
# You should have gotten four people for the last problem. If not, see if why your code doesn't work.
# Else, you can move on to this part, which is, find out how many people have the first letter of their first name start with "A".

a_name = 0

with open("./data_example.csv", encoding="utf-8") as f:
    header = f.readline()
    for line in f:
        current_data = line.strip().split(",")

        if current_data[0][0] == "A":
            a_name += 1

print(f"There are {a_name} people whose first name start with A.")


# Problem 6:
# 19 people! Excellent. How many people come from Guangzhou?

guangzhou_count = 0

with open("./data_example.csv", encoding="utf-8") as f:
    header = f.readline()
    for line in f:
        current_data = line.strip().split(",")
        
        if current_data[-1] == "Guangzhou":
            guangzhou_count += 1

print(f"There are {guangzhou_count} people that come from Guangzhou.")

# Problem 7:
# Just one is from Guangzhou! Alright, last one. How many people have a credit card
# number that is even. There are a couple of ways to solve this.
# You can either do this with the string or with the int.

even_num = 0

with open("./data_example.csv", encoding="utf-8") as f:
    header = f.readline()
    for line in f:
        current_data = line.strip().split(",")
        current_credit_num = int(current_data[-2])

        if current_credit_num % 2 == 0:
            even_num += 1
    

print(f"There are {even_num} people that have a even credit card number.")

# Problem 8:
# Sorry, no answer for the above one. This one is a challenge question.
# Can you design a way to find the most popular food?

food_list = []
score_list = []

with open("./data_example.csv", encoding="utf-8") as f:
    header = f.readline()
    for line in f:
        current_data = line.strip().split(",")
        current_fav_food = current_data[1]
        if current_fav_food in food_list:
            position = food_list.index(current_fav_food)
            score_list[position] += 1               
        else:
            food_list.append(current_fav_food)
            score_list.append(1)

top_food = ""
top_food_score = 0
for food in food_list:
    if score_list[food_list.index(food)] > top_food_score:
        top_food = food
        top_food_score = score_list[food_list.index(top_food)]

print(f"The most popular food is {top_food.lower()} with {top_food_score} votes.")

other_top_food = []
other_top_food_amount = 0

for food in food_list:
    if score_list[food_list.index(food)] == top_food_score:
        if food != top_food:
            other_top_food.append(food)
            other_top_food_amount += 1

for _ in range(other_top_food_amount):
    print(f"The other popular food is {other_top_food[_].lower()} with the same amount of votes.")
