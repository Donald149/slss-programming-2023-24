# Loop Practice
# Author: Donald
# Date: 10 October 2023

# Create a list of groceries
groceries = ["ice cream", "juice", "bread", "waffles"]

# Do something for each thing in the list
# Print it out in a pretty way
# e.g.
#    * ice cream
#      ---
#    * juice
#      ---
#      etc.

# print(f"* {groceries[0]}")
# print(f"  ---")
# print(f"* {groceries[1]}")
# print(f"  ---")
# print(f"* {groceries[2]}")
# print(f"  ---")

for item in groceries:
    print(f"* {item}")
    print(f"  ---")

# Using the above method, create the thing below:
# *
# **
# ***
# ****
# *****
# ******

stars = ["*", "**", "***", "****", "*****", "******"]

for row in stars:
    print(row)

# Problem:
# Create a New Years Countddown that's automated
# Requirements:
#   - starts at 10
#   - counts down every second printing the second it's at
#   - instead of reaching zero, it prints out "Happy New Year"

import time

countdown = ["10", "9", "8", "7", "6", "5", "4", "3", "2", "1"]

for number in countdown:
    print(number)
    time.sleep(1)
print("Happy New Year!")